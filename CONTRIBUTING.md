# Contributing to openQEvo

openQEvo packages scientific code from the QSC Algorithms Thrust into
reusable, tested software. Contributions are welcome from all QSC thrusts
and the broader community.

## Bringing a new method into openQEvo

If you have a time-evolution script you'd like to integrate:

1. **Open an issue** describing the method, its use cases, and a link to
   the original script or paper.
2. A maintainer will work with you to plan the integration.
3. Submit a pull request with:
   - Implementation in `src/openqevo/`
   - Tests in `tests/`
   - An example script in `examples/`
   - A context JSON file in `context/methods/` validated against
     `context/schema/method.schema.json`
     (use `pytest --no-context-validation` while the file is still in progress)

## Development setup

```bash
git clone https://github.com/QSCSoftwareThrust/OpenQEvo.git
cd OpenQEvo
pip install -e ".[dev]"
```

## Running tests

```bash
pytest
```

Method context files are validated against `context/schema/method.schema.json`
by default. Pass `--no-context-validation` when working on an incomplete
context file:

```bash
pytest --no-context-validation
```

## Code style

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting.

```bash
ruff check .
ruff format .
```

## Pull request process

- Open an issue first for non-trivial changes
- Keep PRs focused — one method or fix per PR
- All tests must pass
- Reviewers: Daniel Claudino, Vicente Leyton-Ortega, Samuel Stein
