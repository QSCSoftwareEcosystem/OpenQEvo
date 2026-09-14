"""Spack package for the OpenQEvo development branch.

Add this repository with ``spack repo add /path/to/OpenQEvo/spack`` and install
with ``spack install py-openqevo@main``. Replace the development version with
versioned release checksums when public release artifacts are available.
"""

from spack.package import PythonPackage, depends_on, version


class PyOpenqevo(PythonPackage):
    """Open library for reproducible quantum evolution references."""

    homepage = "https://github.com/QSCSoftwareEcosystem/OpenQEvo"
    git = "https://github.com/QSCSoftwareEcosystem/OpenQEvo.git"

    version("main", branch="main", preferred=True)

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@64:", type="build")
    depends_on("py-numpy@1.24:", type=("build", "run"))
    depends_on("py-scipy@1.10:", type=("build", "run"))
    depends_on("py-jsonschema@4.18:", type=("build", "run"))
