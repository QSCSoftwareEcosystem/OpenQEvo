# openQEvo

**openQEvo** is an open Python library for computing the quantum evolution
operator $e^{-iHt}$. It collects and organizes multiple time-evolution
strategies — Trotterization, QDRIFT, LCU, and others — into a single,
well-documented, and reproducible package.

Developed under the [QSC Software Thrust](https://github.com/QSCSoftwareThrust),
with contributions from the Algorithms Thrust and integration support from
the Applications Thrust.

## Scope

Each method in openQEvo computes the quantum evolution operator for a given
Hamiltonian. The library provides:

- Implementations of multiple time-evolution strategies
- Structured context describing when and how to use each strategy
- Test examples and benchmarks
- AI-ready metadata for tool orchestration (MCP)

## Methods

| Method | Description | Status |
|--------|-------------|--------|
| Trotter-Suzuki | First and higher-order product formulas | Planned |
| QDRIFT | Randomized product formula | Planned |
| *Other* | *Contributed by Algorithms Thrust* | Planned |

## Installation

```bash
pip install openqevo
```

> Note: Package not yet released. See [Contributing](#contributing) to
> get involved.

## Usage

```python
from openqevo import ...
```

## Contributing

openQEvo welcomes contributions from the Algorithms Thrust and the broader
QSC community. Please open an issue before submitting a pull request.

Repository maintained by the
[Software Engineering project](https://github.com/QSCSoftwareThrust/Thrust-Structure/blob/main/ProjectStructure/SE-Structure.md)
of the QSC Software Thrust.

## License

*TBD*
