import math
import re
import time

import requests

from pyuptobox.exceptions import InvalidFileCode


def get_size(bytes_size: int) -> str:
    if bytes_size == 0:
        return "0B"
    name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(bytes_size, 1024)))
    p = math.pow(1024, i)
    s = round(bytes_size / p, 2)
    return f"{s} {name[i]}"


def get_code(value: str) -> str:
    match = re.search(r'https://uptobox\.(?:eu|com)/(\w+)', value)
    if match:
        return match.group(1)
    elif re.match(r"^[a-z0-9]{12}$", value):
        return value
    raise InvalidFileCode(f"Unable to find an identifier: {value}")


def countdown(wait_time: int) -> None:
    while wait_time:
        minutes, seconds = divmod(wait_time, 60)
        timer = f"{minutes}:{seconds}"
        print(timer, end="\r")
        time.sleep(1)
        wait_time -= 1


def get_domain(host: str) -> bool:
    try:
        r = requests.request(method="GET", url=host, timeout=3)
        return True
    except:
        return False
