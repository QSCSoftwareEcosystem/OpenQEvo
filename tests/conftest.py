import openqevo.registry as _registry


def pytest_addoption(parser):
    parser.addoption(
        "--no-context-validation",
        action="store_true",
        default=False,
        help=(
            "Disable JSON schema validation of context files "
            "(for in-progress development)"
        ),
    )


def pytest_configure(config):
    if config.getoption("--no-context-validation", default=False):
        _registry._settings["context_validation"] = False
