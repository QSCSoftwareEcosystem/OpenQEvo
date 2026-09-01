"""Structured evolution outputs, cost accounting, and provenance."""

from __future__ import annotations

import hashlib
import math
import platform
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version
from numbers import Integral
from typing import Any

import numpy as np
import scipy
from numpy.typing import NDArray

EVOLUTION_RESULT_SCHEMA_VERSION = "openqevo-evolution-result/v1"
_OUTPUT_REPRESENTATIONS = {"unitary", "state", "circuit", "operations", "channel"}


@dataclass(frozen=True, slots=True)
class ImplementationProvenance:
    """Identity and dependency versions for one method implementation."""

    package: str
    version: str
    source: str
    backend_versions: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        for name, value in (
            ("package", self.package),
            ("version", self.version),
            ("source", self.source),
        ):
            if not isinstance(value, str) or not value:
                raise ValueError(f"Implementation '{name}' must be a non-empty string.")
        if not isinstance(self.backend_versions, Mapping):
            raise TypeError("'backend_versions' must be a mapping.")
        versions = {
            str(name): str(value) for name, value in self.backend_versions.items()
        }
        object.__setattr__(self, "backend_versions", versions)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "package": self.package,
            "version": self.version,
            "source": self.source,
        }
        if self.backend_versions:
            payload["backend_versions"] = dict(self.backend_versions)
        return payload


@dataclass(frozen=True, slots=True)
class EvolutionCosts:
    """Formula-level and compiled execution costs when they are available."""

    formula_level_pauli_operations: int | None = None
    adjacent_merged_pauli_operations: int | None = None
    compiled_one_qubit_gates: int | None = None
    compiled_two_qubit_gates: int | None = None
    circuit_depth: int | None = None

    def __post_init__(self) -> None:
        for name in (
            "formula_level_pauli_operations",
            "adjacent_merged_pauli_operations",
            "compiled_one_qubit_gates",
            "compiled_two_qubit_gates",
            "circuit_depth",
        ):
            value = getattr(self, name)
            if value is None:
                continue
            if isinstance(value, bool) or not isinstance(value, Integral):
                raise TypeError(f"'{name}' must be an integer or None.")
            if value < 0:
                raise ValueError(f"'{name}' must be non-negative.")
            object.__setattr__(self, name, int(value))

    def to_dict(self) -> dict[str, int | None]:
        return {
            "formula_level_pauli_operations": self.formula_level_pauli_operations,
            "adjacent_merged_pauli_operations": (self.adjacent_merged_pauli_operations),
            "compiled_one_qubit_gates": self.compiled_one_qubit_gates,
            "compiled_two_qubit_gates": self.compiled_two_qubit_gates,
            "circuit_depth": self.circuit_depth,
        }


@dataclass(frozen=True, slots=True)
class EvolutionResult:
    """Method output plus normalized parameters, costs, and reproducibility data."""

    output: Any = field(repr=False, compare=False)
    representation: str
    method_name: str
    implementation: ImplementationProvenance
    parameters: Mapping[str, Any]
    costs: EvolutionCosts = field(default_factory=EvolutionCosts)
    hamiltonian: Mapping[str, Any] = field(default_factory=dict)
    seed: int | None = None
    sampled_sequence: tuple[int, ...] | Sequence[int] | None = None
    runtime_seconds: float | None = None
    environment: Mapping[str, str] = field(default_factory=dict)
    warnings: tuple[str, ...] | Sequence[str] = ()
    limitations: tuple[str, ...] | Sequence[str] = ()

    def __post_init__(self) -> None:
        if self.representation not in _OUTPUT_REPRESENTATIONS:
            choices = ", ".join(sorted(_OUTPUT_REPRESENTATIONS))
            raise ValueError(f"'representation' must be one of: {choices}.")
        if not isinstance(self.method_name, str) or not self.method_name:
            raise ValueError("'method_name' must be a non-empty string.")
        if not isinstance(self.implementation, ImplementationProvenance):
            raise TypeError("'implementation' must be ImplementationProvenance.")
        if not isinstance(self.parameters, Mapping):
            raise TypeError("'parameters' must be a mapping.")
        if not isinstance(self.costs, EvolutionCosts):
            raise TypeError("'costs' must be EvolutionCosts.")
        if not isinstance(self.hamiltonian, Mapping):
            raise TypeError("'hamiltonian' must be a mapping.")
        if not isinstance(self.environment, Mapping):
            raise TypeError("'environment' must be a mapping.")

        seed = self.seed
        if seed is not None:
            if isinstance(seed, bool) or not isinstance(seed, Integral):
                raise TypeError("'seed' must be an integer or None.")
            if seed < 0:
                raise ValueError("'seed' must be non-negative.")
            seed = int(seed)

        sequence = self.sampled_sequence
        if sequence is not None:
            normalized_sequence = tuple(sequence)
            if any(
                isinstance(index, bool) or not isinstance(index, Integral)
                for index in normalized_sequence
            ):
                raise TypeError("'sampled_sequence' must contain integer indices.")
            sequence = tuple(int(index) for index in normalized_sequence)

        runtime = self.runtime_seconds
        if runtime is not None:
            runtime = float(runtime)
            if not math.isfinite(runtime) or runtime < 0:
                raise ValueError("'runtime_seconds' must be non-negative and finite.")

        object.__setattr__(self, "parameters", _json_compatible(self.parameters))
        object.__setattr__(self, "hamiltonian", _json_compatible(self.hamiltonian))
        object.__setattr__(self, "seed", seed)
        object.__setattr__(self, "sampled_sequence", sequence)
        object.__setattr__(self, "runtime_seconds", runtime)
        object.__setattr__(
            self,
            "environment",
            {str(name): str(value) for name, value in self.environment.items()},
        )
        object.__setattr__(self, "warnings", tuple(str(item) for item in self.warnings))
        object.__setattr__(
            self, "limitations", tuple(str(item) for item in self.limitations)
        )

    @property
    def unitary(self) -> NDArray[np.complex128]:
        """Return a dense unitary output or fail clearly for another mode."""
        if self.representation != "unitary":
            raise TypeError("This evolution result does not contain a unitary.")
        return np.asarray(self.output, dtype=complex)

    @property
    def output_sha256(self) -> str | None:
        """Stable hash for NumPy or serializable structured outputs."""
        if isinstance(self.output, np.ndarray):
            array = np.ascontiguousarray(self.output)
            if np.issubdtype(array.dtype, np.complexfloating):
                array = np.ascontiguousarray(array, dtype="<c16")
            return hashlib.sha256(array.tobytes()).hexdigest()
        to_dict = getattr(self.output, "to_dict", None)
        if callable(to_dict):
            import json

            payload = _json_compatible(to_dict())
            encoded = (
                json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"
            ).encode("utf-8")
            return hashlib.sha256(encoded).hexdigest()
        return None

    def to_metadata(self) -> dict[str, Any]:
        """Return the versioned JSON metadata contract without embedding output."""
        output: dict[str, Any] = {"python_type": type(self.output).__name__}
        if isinstance(self.output, np.ndarray):
            output.update(
                {
                    "shape": list(self.output.shape),
                    "dtype": str(self.output.dtype),
                    "sha256": self.output_sha256,
                }
            )
        else:
            to_dict = getattr(self.output, "to_dict", None)
            if callable(to_dict):
                payload = _json_compatible(to_dict())
                output["sha256"] = self.output_sha256
                if isinstance(payload, Mapping):
                    if "schema_version" in payload:
                        output["schema_version"] = payload["schema_version"]
                    if isinstance(payload.get("operations"), list):
                        output["operations"] = len(payload["operations"])
                    if isinstance(payload.get("gates"), list):
                        output["gates"] = len(payload["gates"])
                    if "n_qubits" in payload:
                        output["n_qubits"] = payload["n_qubits"]

        return {
            "schema_version": EVOLUTION_RESULT_SCHEMA_VERSION,
            "representation": self.representation,
            "method": self.method_name,
            "implementation": self.implementation.to_dict(),
            "parameters": dict(self.parameters),
            "costs": self.costs.to_dict(),
            "hamiltonian": dict(self.hamiltonian),
            "seed": self.seed,
            "sampled_sequence": (
                list(self.sampled_sequence)
                if self.sampled_sequence is not None
                else None
            ),
            "runtime_seconds": self.runtime_seconds,
            "environment": dict(self.environment),
            "warnings": list(self.warnings),
            "limitations": list(self.limitations),
            "output": output,
        }


def openqevo_version() -> str:
    """Return the installed package version with a source-tree fallback."""
    try:
        return version("openqevo")
    except PackageNotFoundError:  # pragma: no cover - source import without install
        return "0.1.0+source"


def runtime_environment() -> dict[str, str]:
    """Return stable dependency provenance for reference implementations."""
    return {
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "openqevo": openqevo_version(),
    }


def implementation_provenance(
    source: str,
    *,
    backend_versions: Mapping[str, str] | None = None,
) -> ImplementationProvenance:
    """Build standard OpenQEvo provenance for a registered method."""
    return ImplementationProvenance(
        package="openqevo",
        version=openqevo_version(),
        source=source,
        backend_versions=backend_versions or {},
    )


def installed_versions(packages: Sequence[str]) -> dict[str, str]:
    """Resolve installed backend distribution versions for result provenance."""
    resolved = {}
    for package in packages:
        try:
            resolved[package] = version(package)
        except PackageNotFoundError:
            resolved[package] = "unknown"
    return resolved


def _json_compatible(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_compatible(item) for key, item in value.items()}
    if isinstance(value, np.ndarray):
        return [_json_compatible(item) for item in value.tolist()]
    if isinstance(value, (tuple, list)):
        return [_json_compatible(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError(
        "Result metadata value of type "
        f"{type(value).__name__!r} is not JSON-compatible."
    )
