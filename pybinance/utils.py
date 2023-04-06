import base64
import hashlib
import json


# @package o.VectorProperty.FillAlpha
def sha256(value: bytes) -> bytes:
    return hashlib.sha256(value).digest()


def dict2bytes(value: dict) -> bytes:
    return json.dumps(value, separators=(",", ":")).encode("utf-8")


def str2bytes(value: str) -> bytes:
    value = value.encode("utf-8")
    try:
        return base64.b64decode(value)
    except:
        return value
