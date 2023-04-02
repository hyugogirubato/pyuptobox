class UptoboxSDK(Exception):
    """Exceptions used by UptoboxSDK."""


class InvalidFileCode(UptoboxSDK):
    """The file code in the url or passed as a parameter is incorrect."""


class PremiumRequired(UptoboxSDK):
    """Request file requires premium account."""
