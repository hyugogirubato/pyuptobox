from __future__ import annotations

import json
from pathlib import Path
import re

import requests
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder
from pyuptobox.exceptions import InvalidCredentials


class Client:
    HEADERS = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }

    def __init__(self):
        self._token = None
        self._web = "https://uptobox.com"
        self._api = f"{self._web}/api"
        self._session = requests.Session()

    def _request(self, **kwargs) -> dict:
        params = kwargs.get("params", {})
        if self._token is not None:
            params["token"] = self._token

        r = self._session.request(
            method=kwargs.get("method", "GET").upper(),
            url=kwargs.get("url", self._api),
            params=params,
            data=kwargs.get("data", None),
            headers=kwargs.get("headers", Client.HEADERS))

        content = r.json()
        if content.get("statusCode", 0) in [0, 18, 22, 24, 39]:
            return content
        raise Exception(r.text)

    def login(self, **kwargs) -> dict:
        login = kwargs.get("login", None)
        password = kwargs.get("password", None)
        token = kwargs.get("token", None)
        xfss = kwargs.get("xfss", None)
        if login is not None and password is not None:
            r = self._session.request(
                method="POST",
                url=f"{self._web}/login",
                data={"login": login, "password": password}
            )
            if "My account" not in r.text:
                raise InvalidCredentials("Invalid password/login")
        elif token is not None:
            self._token = token
        elif xfss is not None:
            self._session.cookies.set("xfss", xfss)
        else:
            raise InvalidCredentials("Invalid login credentials")

        if token is None:
            r = self._session.request(method="GET", url=f"{self._web}/my_account")
            soup = BeautifulSoup(r.content, "html.parser")
            content_wrapper_div = soup.find("div", {"id": "content-wrapper"})
            data_ui = json.loads(content_wrapper_div.select_one(".width-content")["data-ui"])
            self._token = data_ui["token"]
        return self.get_user()

    def get_user(self) -> dict:
        return self._request(url=f"{self._api}/user/me")["data"]

    def set_ssl_download(self, ssl: bool = True) -> None:
        self._request(method="PATCH", url=f"{self._api}/user/settings", params={"ssl": int(ssl)})

    def set_direct_download(self, direct: bool = True) -> None:
        self._request(method="PATCH", url=f"{self._api}/user/settings", params={"directDownload": int(direct)})

    def set_miniature_uts(self, miniature: bool = True) -> None:
        self._request(method="PATCH", url=f"{self._api}/user/settings", params={"miniatureUts": int(miniature)})

    def set_notif_deletions(self, notif: bool = False) -> None:
        self._request(method="PATCH", url=f"{self._api}/user/settings", params={"notifDeletions": int(notif)})

    def set_security_lock(self, lock: bool = False) -> None:
        self._request(method="PATCH", url=f"{self._api}/user/securityLock", params={"securityLock": int(lock)})

    def get_point_conversion(self, points: int = 10) -> dict:
        if points not in [10, 25, 50, 100]:
            raise ValueError("The number of points passed in parameter is incompatible.")
        return self._request(url=f"{self._api}/user/requestPremium", params={"points": points})["data"]

    def get_voucher(self, time: int = 30, quantity: int = 1) -> list:
        if time not in [30, 365, 730]:
            raise ValueError("The duration is invalid.")
        return self._request(url=f"{self._api}/user/createVoucher", params={
            "time": f"{time}d",
            "quantity": quantity
        })["data"]

    def get_file_link(self, file_code: str, waiting_token: str = None) -> dict:
        params = {"file_code": file_code}
        if waiting_token is not None:
            params["waitingToken"] = waiting_token
        return self._request(url=f"{self._api}/link")["data"]

    def get_file_info(self, file_codes: list) -> list:
        return self._request(url=f"{self._api}/link/info", params={"fileCodes": ",".join(file_codes)})["data"]["list"]

    def get_public_folders(self, folder: str, hash: str, limit: int = 10, offset: int = 0) -> list:
        return self._request(url=f"{self._api}/user/public", params={
            "folder": folder,
            "hash": hash,
            "limit": limit,
            "offset": offset
        })["data"]["list"]

    def get_public_files(self, path: str, limit: int = 10, offset: int = 0, order: str = "file_name", dir: str = "asc") -> dict:
        if order not in ["file_name", "file_size", "file_size", "file_downloads", "transcoded"]:
            raise ValueError("Invalid order value.")
        if dir not in ["asc", "desc"]:
            raise ValueError("Invalid dir value.")

        return self._request(url=f"{self._api}/user/files", params={
            "path": path,
            "limit": limit,
            "offset": offset,
            "orderBy": order,
            "dir": dir
        })["data"]

    def set_file_info(self, file_code: str, public: bool = None, name: str = None, description: str = None, password: str = None) -> bool:
        params = {"file_code": file_code}
        if public is not None:
            params["public"] = int(public)
        if name is not None:
            params["new_name"] = name
        if description is not None:
            params["description"] = description
        if password is not None:
            params["password"] = password
        return self._request(method="PATCH", url=f"{self._api}/user/files", params=params)["data"]["updated"] == 1

    def set_public_files(self, file_codes: list, public: bool = False) -> bool:
        return self._request(method="PATCH", url=f"{self._api}/user/files", params={
            "file_codes": ",".join(file_codes),
            "public": int(public)
        })["data"]["updated"] == len(file_codes)

    def move_folder(self, source: int, destination: int) -> None:
        self._request(method="PATCH", url=f"{self._api}/user/files", params={
            "fld_id": source,
            "destination_fld_id": destination,
            "action": "move"
        })

    def move_files(self, file_codes: list, folder: int) -> bool:
        return self._request(method="PATCH", url=f"{self._api}/user/files", params={
            "file_codes": ",".join(file_codes),
            "destination_fld_id": folder,
            "action": "move"
        })["data"]["updated"] == len(file_codes)

    def copy_files(self, file_codes: list, folder: int) -> bool:
        return self._request(method="PATCH", url=f"{self._api}/user/files", params={
            "file_codes": ",".join(file_codes),
            "destination_fld_id": folder,
            "action": "copy"
        })["data"]["updated"] == len(file_codes)

    def rename_folder(self, folder: int, name: str) -> None:
        self._request(method="PATCH", url=f"{self._api}/user/files", params={"fld_id": folder, "new_name": name})

    def create_folder(self, path: str) -> None:
        self._request(method="PUT", url=f"{self._api}/user/files", params={"path": path, "name": "newFolder"})

    def delete_files(self, file_codes: list) -> None:
        self._request(method="DELETE", url=f"{self._api}/user/files", params={"file_codes": ",".join(file_codes)})

    def delete_folder(self, folder: int) -> None:
        self._request(method="DELETE", url=f"{self._api}/user/files", params={"fld_id": folder})

    def upload(self, path: Path) -> dict:
        multi = MultipartEncoder(fields={"files": (path.name, open(path, "rb"))})
        headers = Client.HEADERS.copy()
        headers["content-type"] = multi.content_type
        return self._request(
            method="POST",
            url="https:" + self._request(url=f"{self._api}/upload")["data"]["uploadLink"],
            data=multi,
            headers=headers
        )["files"]

    def get_pin(self, file_code: str) -> dict:
        return self._request(url=f"{self._api}/streaming", params={"file_code": file_code})["data"]

    def check_pin(self, pin: str, hash: str) -> dict:
        return self._request(url=f"{self._api}/streaming", params={"pin": pin, "check": hash})["data"]

    def transcode(self, file_code: str) -> dict:
        return self._request(url=f"{self._api}/upload/transcode/id", params={"file_code": file_code})["data"]

    def get_all_files(self) -> list:
        return self._request(url=f"{self._api}/user/files/all")["data"]

    def add_file(self, file_code: str) -> None:
        self._request(url=f"{self._api}/user/file/alias", params={"file_code": file_code})

    def get_stream(self, file_code: str) -> list:
        KEYS = ["base", "id", "name"]
        lines = self._request(url=f"https://uptostream.com/api/streaming/source/get", params={
            "file_code": file_code
        })["data"]["sources"].split("\n")

        items = []
        item = {}
        for i in range(len(lines)):
            if "function baseLink()" in lines[i]:
                if item != {}:
                    items.append(item)
                    item = {}
                item["base"] = lines[i + 1]
            elif "function id()" in lines[i]:
                item["id"] = lines[i + 1]
            elif "function name()" in lines[i]:
                item["name"] = lines[i + 1]
            elif "var label" in lines[i]:
                item["label"] = lines[i]
            elif "var kind" in lines[i]:
                item["kind"] = lines[i]
            elif "var srclang" in lines[i]:
                item["lang"] = lines[i]
            elif "var format" in lines[i]:
                item["format"] = lines[i]
        items.append(item)
        for i in range(len(items)):
            for key in items[i].keys():
                items[i][key] = re.search(r'"(.*?)"', items[i][key]).group(1)

            if all([key in items[i] for key in KEYS]):
                items[i]["link"] = "{base}/stream/{id}/{name}".format(
                    base=items[i]["base"],
                    id=items[i]["id"],
                    name=items[i]["name"]
                )
                for key in KEYS:
                    del items[i][key]
        return items
