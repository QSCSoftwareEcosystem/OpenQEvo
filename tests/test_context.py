"""Tests for context JSON loading and schema validation."""

import json
import re
from pathlib import Path

import jsonschema
import pytest

import openqevo
import openqevo.registry as _registry

CONTEXT_DIR = Path(__file__).resolve().parent.parent / "context"
METHOD_CONTEXT_DIR = CONTEXT_DIR / "methods"
METHOD_SCHEMA_PATH = CONTEXT_DIR / "schema" / "method.schema.json"
KEY_POINT_SCHEMA_PATH = CONTEXT_DIR / "schema" / "key_point.schema.json"
SELECTION_RULE_SCHEMA_PATH = CONTEXT_DIR / "schema" / "selection_rule.schema.json"
WIKI_MANIFEST_SCHEMA_PATH = CONTEXT_DIR / "schema" / "wiki_manifest.schema.json"
RECOMMENDATION_SCHEMA_PATH = CONTEXT_DIR / "schema" / "recommendation.schema.json"
RECOMMENDATION_EXAMPLES_DIR = CONTEXT_DIR / "selection" / "recommendation_examples"
SOFTWARE_SOURCE_INVENTORY_PATH = CONTEXT_DIR / "software" / "source_inventory.md"
KEY_POINT_DIRS = (
    CONTEXT_DIR / "trotterization" / "key_points",
    CONTEXT_DIR / "randomized_methods" / "key_points",
    CONTEXT_DIR / "interaction_picture" / "key_points",
    CONTEXT_DIR / "annealing" / "key_points",
)
WIKI_DIRS = (
    CONTEXT_DIR / "trotterization" / "wiki",
    CONTEXT_DIR / "randomized_methods" / "wiki",
    CONTEXT_DIR / "interaction_picture" / "wiki",
    CONTEXT_DIR / "annealing" / "wiki",
)


def _key_point_paths():
    for key_point_dir in KEY_POINT_DIRS:
        yield from key_point_dir.glob("*.json")


def _key_point_ids():
    return {json.loads(path.read_text())["id"] for path in _key_point_paths()}


class TestContextLoading:
    def test_trotter_s1_context_loads(self):
        method = openqevo.get("trotter_s1")
        ctx = method.context
        assert ctx is not None
        assert ctx["method_name"] == "trotter_s1"
        assert ctx["source"] == "algorithms-thrust"
        assert "parameters" in ctx
        assert "steps" in ctx["parameters"]

    def test_trotter_s2_context_loads(self):
        method = openqevo.get("trotter_s2")
        ctx = method.context
        assert ctx is not None
        assert ctx["method_name"] == "trotter_s2"
        assert "error_scaling" in ctx["complexity"]

    def test_exact_context_loads(self):
        method = openqevo.get("exact")
        ctx = method.context
        assert ctx is not None
        assert ctx["source"] == "openqevo"

    def test_context_validates_against_schema(self):
        """All method context files must fully validate against method.schema.json.

        Pass --no-context-validation to pytest to skip (for in-progress development).
        """
        if not _registry._settings["context_validation"]:
            pytest.skip("context validation disabled via --no-context-validation")

        with open(METHOD_SCHEMA_PATH) as f:
            schema = json.load(f)

        for json_file in METHOD_CONTEXT_DIR.glob("*.json"):
            with open(json_file) as f:
                ctx = json.load(f)
            jsonschema.validate(instance=ctx, schema=schema)

    def test_all_registered_methods_have_context(self):
        """Every registered method should have a context JSON file."""
        for name in openqevo.list_methods():
            method = openqevo.get(name)
            assert method.context is not None, (
                f"Method '{name}' from source '{method.source}' has no context file"
            )

    def test_method_execution_metadata_matches_registry(self):
        """Executable method metadata must align with the OpenQEvo registry."""
        registered_methods = set(openqevo.list_methods())

        for json_file in METHOD_CONTEXT_DIR.glob("*.json"):
            with open(json_file) as f:
                ctx = json.load(f)

            execution = ctx.get("execution")
            if execution is None:
                continue

            method_name = execution["method_name"]
            if execution["implemented"]:
                if method_name not in registered_methods:
                    assert ctx["source"] in {"qiskit", "pennylane", "qrack"}, (
                        f"{json_file} marks {method_name} executable, but it is "
                        "not registered"
                    )
                    assert any(
                        "optional dependency" in requirement
                        for requirement in execution.get("backend_requirements", [])
                    )
                    continue
                assert execution["entrypoint"].startswith("openqevo.get(")
            else:
                assert method_name not in registered_methods
                assert execution.get("non_executable_reason")

    def test_method_local_references_exist(self):
        """Method metadata can cite local context files, which must exist."""
        for json_file in METHOD_CONTEXT_DIR.glob("*.json"):
            with open(json_file) as f:
                ctx = json.load(f)

            for reference in ctx.get("references", []):
                url = reference.get("url", "")
                if url.startswith(".."):
                    target = json_file.parent / url
                    assert target.exists(), (
                        f"{json_file} cites missing local reference {url}"
                    )

    def test_key_points_validate_and_link_to_raw_data(self):
        """Extracted key points must validate and cite existing raw data."""
        with open(KEY_POINT_SCHEMA_PATH) as f:
            schema = json.load(f)

        for json_file in _key_point_paths():
            with open(json_file) as f:
                key_point = json.load(f)

            jsonschema.validate(instance=key_point, schema=schema)

            for evidence in key_point["evidence"]:
                source_path = (json_file.parent / evidence["source"]).resolve()
                assert source_path.exists(), (
                    f"{json_file} cites missing evidence {evidence['source']}"
                )

    def test_selection_rules_validate_and_reference_key_points(self):
        """Selection rules must validate and reference known key-point IDs."""
        with open(SELECTION_RULE_SCHEMA_PATH) as f:
            schema = json.load(f)

        rules_path = CONTEXT_DIR / "selection" / "rules.json"
        with open(rules_path) as f:
            rules = json.load(f)

        jsonschema.validate(instance=rules, schema=schema)

        key_point_ids = _key_point_ids()
        for rule in rules["rules"]:
            for key_point_id in rule.get("key_points", []):
                assert key_point_id in key_point_ids, (
                    f"{rule['id']} references unknown key point {key_point_id}"
                )

    def test_wiki_manifest_validates_and_paths_exist(self):
        """The wiki manifest must validate and point to existing paths."""
        with open(WIKI_MANIFEST_SCHEMA_PATH) as f:
            schema = json.load(f)

        manifest_path = CONTEXT_DIR / "wiki_manifest.json"
        with open(manifest_path) as f:
            manifest = json.load(f)

        jsonschema.validate(instance=manifest, schema=schema)

        for collection in manifest["collections"]:
            for field in ("raw_data", "key_points", "wiki", "selection_rules"):
                target = CONTEXT_DIR / collection[field]
                assert target.exists(), (
                    f"Manifest collection {collection['id']} has missing "
                    f"{field}: {collection[field]}"
                )

    def test_recommendation_schema_validates_executable_payload(self):
        """LLM recommendations should validate against the output schema."""
        with open(RECOMMENDATION_SCHEMA_PATH) as f:
            schema = json.load(f)

        recommendation = {
            "recommendation_id": "example-qdrift",
            "method_name": "qdrift",
            "method_family": "randomized_methods",
            "executable": True,
            "confidence": "medium",
            "parameters": {"samples": 100, "seed": 7},
            "required_inputs": [],
            "execution": {
                "implemented": True,
                "method_name": "qdrift",
                "entrypoint": "openqevo.get(\"qdrift\").evolve(terms, t, **parameters)",
                "input_representation": ["matrix_terms"],
                "required_arguments": ["terms", "t", "samples"],
            },
            "rationale": [
                "qDRIFT is the registered randomized baseline for many-term "
                "Hamiltonians."
            ],
            "warnings": ["Sweep sample count before final accuracy claims."],
            "evidence": [
                {
                    "key_point_id": "qdrift-randomized-scaling",
                    "source": (
                        "randomized_methods/raw_data/"
                        "openqevo-randomized-qdrift-campbell-2019-1811.08017.md"
                    ),
                    "note": "Supports qDRIFT term-weighted randomized simulation.",
                }
            ],
            "alternatives": [
                {
                    "method_name": "trotter_s2",
                    "reason": (
                        "Deterministic baseline with different depth/error tradeoff."
                    ),
                    "executable": True,
                }
            ],
        }

        jsonschema.validate(instance=recommendation, schema=schema)

    def test_recommendation_examples_validate_against_schema(self):
        """Checked-in recommendation examples must match the schema."""
        with open(RECOMMENDATION_SCHEMA_PATH) as f:
            schema = json.load(f)

        examples = sorted(RECOMMENDATION_EXAMPLES_DIR.glob("*.json"))
        assert examples, "Expected at least one recommendation example"

        for example_path in examples:
            with open(example_path) as f:
                recommendation = json.load(f)
            jsonschema.validate(instance=recommendation, schema=schema)

    def test_software_source_inventory_links_to_existing_raw_docs(self):
        """Software source inventory must cite existing local raw docs."""
        text = SOFTWARE_SOURCE_INVENTORY_PATH.read_text()
        links = re.findall(r"\]\((raw_data/[^)]+\.md)\)", text)
        assert links, "Expected software source inventory to link raw docs"

        for link in links:
            raw_doc = SOFTWARE_SOURCE_INVENTORY_PATH.parent / link
            assert raw_doc.exists(), f"Missing software raw doc: {link}"
            assert raw_doc.stat().st_size > 0, f"Empty software raw doc: {link}"

    def test_wiki_pages_reference_known_key_points(self):
        """Wiki pages should cite known key-point IDs when making claims."""
        key_point_ids = _key_point_ids()

        for wiki_dir in WIKI_DIRS:
            wiki_pages = sorted(wiki_dir.glob("*.md"))
            assert wiki_pages, f"Expected at least one wiki page in {wiki_dir}"

            for page in wiki_pages:
                text = page.read_text()
                if page.name in {"changelog.md", "open_questions.md"}:
                    continue
                assert any(key_point_id in text for key_point_id in key_point_ids), (
                    f"{page} does not reference any known key-point ID"
                )
