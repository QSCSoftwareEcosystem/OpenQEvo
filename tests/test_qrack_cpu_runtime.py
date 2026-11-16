"""Real PyQrack CPU checks, enabled by OPENQEVO_TEST_QRACK_RUNTIME=1.

Each check runs in a fresh process so the fake PyQrack unit-test fixtures cannot
replace the native runtime. When enabled, missing dependencies and runtime
errors fail the test; CI installs the optional extra explicitly.
"""

from __future__ import annotations

import os
import subprocess
import sys

import pytest

pytestmark = pytest.mark.skipif(
    os.environ.get("OPENQEVO_TEST_QRACK_RUNTIME") != "1",
    reason="Set OPENQEVO_TEST_QRACK_RUNTIME=1 with the qrack extra installed.",
)

_CPU_CHECK = """
import sys

import numpy as np
import pyqrack
from scipy.linalg import expm

import openqevo

assert pyqrack.__file__, "Expected the installed PyQrack module"
order = int(sys.argv[1])
method = openqevo.get("qrack_trotter")
reference = openqevo.get(f"trotter_s{order}")

# Single Pauli exponentials are analytic controls for sign, coefficient,
# imaginary Y basis changes, qubit order, and multi-qubit parity rotations.
for word in ("X", "Y", "Z", "XI", "IY", "XY", "YZ", "II"):
    hamiltonian = openqevo.PauliHamiltonian(
        identifier=f"qrack-cpu-{word}",
        terms=(openqevo.PauliTerm(-0.7, word),),
    )
    result = method.evolve(
        hamiltonian, t=0.35, steps=1, order=order, is_gpu=False
    )
    expected = expm(-1j * hamiltonian.dense_terms()[0] * 0.35)
    np.testing.assert_allclose(result, expected, atol=3e-6, rtol=0)

# A noncommuting input exercises both product orders and repeated native calls.
hamiltonian = openqevo.PauliHamiltonian(
    identifier="qrack-cpu-noncommuting",
    terms=(
        openqevo.PauliTerm(0.7, "XY"),
        openqevo.PauliTerm(-0.3, "IZ"),
        openqevo.PauliTerm(0.2, "YI"),
    ),
)
result = method.evolve(
    hamiltonian, t=0.35, steps=6, order=order, is_gpu=False
)
expected = reference.evolve(hamiltonian, t=0.35, steps=6)
# Distributed PyQrack wheels may use float32 internally.
np.testing.assert_allclose(result, expected, atol=1e-5, rtol=0)
np.testing.assert_allclose(result.conj().T @ result, np.eye(4), atol=1e-5, rtol=0)
"""


@pytest.mark.parametrize("order", [1, 2])
def test_qrack_real_cpu_matches_analytic_and_native_controls(order):
    result = subprocess.run(
        [sys.executable, "-c", _CPU_CHECK, str(order)],
        capture_output=True,
        text=True,
        timeout=90,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
