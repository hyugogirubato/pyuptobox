import math
import re
import time

from UptoboxSDK.exceptions import InvalidFileCode


def get_size(bytes_size: int) -> str:
    if bytes_size == 0:
        return "0B"
    name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(bytes_size, 1024)))
    p = math.pow(1024, i)
    s = round(bytes_size / p, 2)
    return f"{s} {name[i]}"


def get_code(code: str) -> str:
    if code.startswith("https://uptobox.com/") or code.startswith("https://uptostream.com/"):
        code = re.search(r"\.com/(\w+)", code).group(1)
    if code is None or len(code) != 12:
        raise InvalidFileCode("The file code format is invalid")
    return code


def get_input_bool(message: str, default=True) -> bool:
    answer = str(input(f"{message} [{default}]: ")).lower()
    if answer == "":
        return default
    return answer in ["y", "yes", "t", "true", "1"]


def countdown(wait_time: int) -> None:
    while wait_time:
        minutes, seconds = divmod(wait_time, 60)
        timer = f"{minutes}:{seconds}"
        print(timer, end="\r")
        time.sleep(1)
        wait_time -= 1
