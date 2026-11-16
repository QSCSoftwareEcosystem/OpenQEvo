"""Bundle runtime knowledge-base records and their local evidence dependencies.

The editable source tree keeps ``context/`` as its authoritative knowledge
base. Wheels receive a private copy so method discovery never depends on the
current working directory. This includes inventories and the Markdown/CSV
sources they link, including legacy discovery surveys. PDF/image companions
and conversion scratch under ``tmp/`` remain source-corpus material and are
not bundled. The sdist retains the selected textual context for rebuilding.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit

from setuptools.command.build_py import build_py


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from _strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)


def context_files(root: Path) -> list[Path]:
    """Select runtime records plus transitive, existing local evidence files."""
    root = root.resolve()
    selected = set()
    pending = []
    for directory in ("methods", "schema", "selection"):
        pending.extend((root / directory).rglob("*.json"))

    manifest = root / "wiki_manifest.json"
    if manifest.is_file():
        pending.append(manifest)
        for collection in json.loads(manifest.read_text(encoding="utf-8"))[
            "collections"
        ]:
            for section in ("key_points", "wiki"):
                if section not in collection:
                    continue
                directory = root / collection[section]
                pending.extend(directory.glob("*.json"))
                pending.extend(directory.glob("*.md"))

    # Selection rules cite key-point IDs; preserve their curated evidence chain.
    pending.extend(root.glob("*/key_points/*.json"))
    while pending:
        path = pending.pop().resolve()
        if path in selected or not path.is_file() or not path.is_relative_to(root):
            continue
        if "tmp" in path.relative_to(root).parts:
            continue
        selected.add(path)
        content = path.read_text(encoding="utf-8")
        references = (
            _strings(json.loads(content))
            if path.suffix == ".json"
            else re.findall(r"\]\(([^)]+)\)", content)
        )
        for reference in references:
            if not reference.split("#", 1)[0].endswith((".json", ".md", ".csv")):
                continue
            parsed = urlsplit(reference)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            relative = Path(unquote(parsed.path))
            for base in (path.parent, path.parent.parent, root):
                candidate = (base / relative).resolve()
                if candidate.is_relative_to(root) and candidate.is_file():
                    pending.append(candidate)
                    break
    return sorted(selected)


class BuildPy(build_py):
    """Copy knowledge-base records after setuptools builds Python modules."""

    def run(self):
        super().run()
        root = Path(__file__).resolve().parent.parent / "context"
        destination = Path(self.build_lib) / "openqevo" / "_context"
        # A previous build may have selected files no longer referenced today.
        if destination.exists():
            shutil.rmtree(destination)
        for source in context_files(root):
            target = destination / source.relative_to(root)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def get_outputs(self, include_bytecode=1):
        outputs = super().get_outputs(include_bytecode)
        destination = Path(self.build_lib) / "openqevo" / "_context"
        return outputs + [
            str(path) for path in destination.rglob("*") if path.is_file()
        ]
