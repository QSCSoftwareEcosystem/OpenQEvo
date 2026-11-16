"""Verify installed distribution behavior from outside the source checkout.

Usage: python /path/to/OpenQEvo/packaging/check_installed.py
Run with the built wheel installed, from an unrelated working directory.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import numpy as np

import openqevo
from openqevo.registry import CONTEXT_DIR


def main() -> None:
    source_root = Path(__file__).resolve().parent.parent
    package_path = Path(openqevo.__file__).resolve()
    assert not package_path.is_relative_to(source_root), package_path
    assert CONTEXT_DIR == package_path.parent / "_context", CONTEXT_DIR

    def read(relative):
        return json.loads((CONTEXT_DIR / relative).read_text(encoding="utf-8"))

    manifest = read("wiki_manifest.json")
    jsonschema.validate(manifest, read("schema/wiki_manifest.schema.json"))
    evidence_count = 0
    for collection in manifest["collections"]:
        for section in ("wiki", "key_points", "raw_data"):
            if section not in collection:
                continue
            assert (CONTEXT_DIR / collection[section]).is_dir(), collection
        if "key_points" not in collection:
            continue
        for path in (CONTEXT_DIR / collection["key_points"]).glob("*.json"):
            key_point = json.loads(path.read_text(encoding="utf-8"))
            jsonschema.validate(key_point, read("schema/key_point.schema.json"))
            for evidence in key_point["evidence"]:
                assert (path.parent / evidence["source"]).is_file(), evidence
                evidence_count += 1

    for path in (CONTEXT_DIR / "methods").glob("*.json"):
        context = json.loads(path.read_text(encoding="utf-8"))
        jsonschema.validate(context, read("schema/method.schema.json"))
        for reference in context.get("references", []):
            url = reference.get("url", "")
            if url.startswith(".."):
                assert (path.parent / url).is_file(), reference
    for name in openqevo.list_methods():
        assert openqevo.get(name).context is not None, name

    jsonschema.validate(
        read("selection/rules.json"), read("schema/selection_rule.schema.json")
    )
    for path in (CONTEXT_DIR / "selection/recommendation_examples").glob("*.json"):
        recommendation = json.loads(path.read_text(encoding="utf-8"))
        jsonschema.validate(recommendation, read("schema/recommendation.schema.json"))
        if recommendation["executable"]:
            result = openqevo.execute_recommendation(recommendation, structured=True)
            assert np.isfinite(result.unitary).all()
            json.dumps(result.to_metadata())

    # The documented quick start must carry context as well as a dense output.
    hamiltonian = openqevo.PauliHamiltonian(
        identifier="quickstart-xz",
        terms=(openqevo.PauliTerm(1.0, "X"), openqevo.PauliTerm(1.0, "Z")),
    )
    exact = openqevo.get("exact").run(hamiltonian, t=1.0)
    approximation = openqevo.get("trotter_s2").run(hamiltonian, t=1.0, steps=20)
    assert approximation.unitary.shape == exact.unitary.shape == (2, 2)
    assert np.linalg.norm(approximation.unitary - exact.unitary) < 0.01
    assert approximation.costs.formula_level_pauli_operations == 80
    print(f"Installed wheel: {package_path}")
    print(f"Validated {len(manifest['collections'])} knowledge-base collections")
    print(f"Resolved {evidence_count} local evidence links")
    print("Method context, recommendations, and quick start passed")


if __name__ == "__main__":
    main()
