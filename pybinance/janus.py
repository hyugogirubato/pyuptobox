import time
import uuid
from enum import Enum
from typing import Union
from urllib.parse import urlparse, urlencode

import jwt

from pybinance import pygzip
from pybinance.exceptions import InvalidService, UnregisteredService
from pybinance.utils import sha256, dict2bytes, str2bytes


class KEY(Enum):
    SAASEXCH = b'oKpDfrjhHCEfOzDVRBsVHDKZoyAyxWhPLHCKNOgN'
    BINANCE = b'KrBcVcDqlIlqZPpwDMtiRIGvnOEsvuPKmavNUbaK'


def _get_payload(value: Union[bytes, str, dict]) -> bytes:
    if value is None:
        value = b''
    else:
        if isinstance(value, dict):
            value = dict2bytes(value)
        if isinstance(value, str):
            value = str2bytes(value)
        value = pygzip.compress(
            value,
            level=9,
            timestamp=0,
            extra_flags=pygzip.FLAG.FTEXT,
            operating_system=pygzip.OPERATING_SYSTEM.FAT
        )
    return sha256(value)


class Janus:

    def __init__(self, key: KEY = None):
        self._key = key

    def get_dig(self, url: str, **kwargs) -> bytes:
        method = kwargs.get("method", "GET").upper()
        params = kwargs.get("params", None)
        data = kwargs.get("data", None)

        if url.startswith("https://api.saasexch.cc"):
            self._key = KEY.SAASEXCH
        elif url.startswith("https://www.binance.info"):
            self._key = KEY.BINANCE
        else:
            raise InvalidService("Unrecognized/unsupported service.")

        return sha256("\n".join([
            method,  # METHOD
            urlparse(url).path + "/",  # PATH
            urlencode(params or {}, doseq=True),  # QUERY
            _get_payload(data).hex()  # GZIP/SHA256/BODY
        ]).encode("utf-8"))

    # @package o.getDoubleTapTimeoutMillis;
    def get_jwt(self, dig: bytes) -> str:
        current = round(time.time())

        payload = {
            "exp": current,  # EXPIRATION
            "iat": current,  # ISSUED_AT
            "ts": current,
            "jti": str(uuid.uuid4()),  # ID
            "dig": dig.hex()
        }
        if self._key == KEY.SAASEXCH:
            payload["exp"] += 120
            payload["ts"] += 60
            payload["iss"] = "cburg0n9gpbp8ciciok0"  # ISSUER
        elif self._key == KEY.BINANCE:
            payload["exp"] += 86400000
            payload["ts"] += -5
            payload["iss"] = "byshBKEMk3Yo7uTpxbSv67"  # ISSUER

        if self._key is None:
            raise UnregisteredService("The service has not been initialized.")
        return jwt.encode(payload, self._key.value, algorithm="HS256")
