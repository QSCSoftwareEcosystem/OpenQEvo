# OpenQEvo Spack repository

This directory is a self-contained Spack repository for the current
development branch of OpenQEvo.

```bash
spack repo add /path/to/OpenQEvo/spack
spack install py-openqevo@main
```

The package intentionally tracks `main` until OpenQEvo has a chosen license
and a tagged public release. Before submitting it to the builtin Spack
repository, replace the development version with one or more immutable release
versions and checksums, then test the concretized environment on the supported
HPC platforms.
