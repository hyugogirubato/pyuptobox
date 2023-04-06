class PyUptobox(Exception):
    """Exceptions used by pyuptobox."""


class InvalidCredentials(PyUptobox):
    """Invalid Credentials."""


class InvalidFileCode(PyUptobox):
    """The file code in the url or passed as a parameter is incorrect."""
