class PyBinance(Exception):
    """Exceptions used by pybinance."""


class InvalidService(PyBinance):
    """No JWT key available for service."""


class UnregisteredService(PyBinance):
    """No service has been initialized."""
