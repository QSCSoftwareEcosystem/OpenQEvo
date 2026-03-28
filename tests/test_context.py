"""Tests for context JSON loading and schema validation."""

import json
from pathlib import Path

import openqevo

CONTEXT_DIR = Path(__file__).resolve().parent.parent / "context"


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

    def test_context_has_required_fields(self):
        """All context files must have the fields required by schema.json."""
        schema_path = CONTEXT_DIR / "schema.json"
        with open(schema_path) as f:
            schema = json.load(f)
        required_fields = schema["required"]

        for json_file in CONTEXT_DIR.glob("*.json"):
            if json_file.name == "schema.json":
                continue
            with open(json_file) as f:
                ctx = json.load(f)
            for field in required_fields:
                assert field in ctx, (
                    f"{json_file.name} missing required field '{field}'"
                )

    def test_all_registered_methods_have_context(self):
        """Every registered native method should have a context JSON file."""
        for name in openqevo.list_methods():
            method = openqevo.get(name)
            if method.source in ("algorithms-thrust", "openqevo"):
                assert method.context is not None, (
                    f"Method '{name}' has no context file"
                )
