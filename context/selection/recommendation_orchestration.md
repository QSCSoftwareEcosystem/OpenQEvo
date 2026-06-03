# Recommendation Orchestration Boundary

OpenQEvo should own the context stack, method metadata, selection-rule source material, and execution bridge for already-selected methods. The preferred architecture is for recommendation/search orchestration to live in an external AS/MCP/RAG layer.

## OpenQEvo responsibilities

- Maintain `context/` raw evidence, key points, wiki pages, method metadata, and selection rules.
- Keep `context/methods/*["execution"]["method_name"]` aligned with `openqevo.get(name)`.
- Provide `openqevo.execute_recommendation(...)` for executable recommendation objects.
- Validate context schemas and recommendation payload shape.

## External AS responsibilities

- Retrieve relevant context from OpenQEvo and QAppsWiki.
- Rank applicable methods from user query, Hamiltonian features, backend constraints, and evidence.
- Emit recommendation JSON conforming to `context/schema/recommendation.schema.json`.
- Decide whether to execute through OpenQEvo, ask the user for missing inputs, or return a non-executable/planned-method explanation.

## Current decision

Project preference is external AS orchestration. OpenQEvo should not grow a full RAG/search/recommendation agent until the project explicitly decides otherwise.
