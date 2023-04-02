import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder

from UptoboxSDK.exceptions import PremiumRequired
from UptoboxSDK.utils import get_size, get_code, get_input_bool, countdown


class Client:
    HEADERS = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }

    def __init__(self):
        self._token = None
        self._session = requests.Session()
        self._web = "https://uptobox.com"
        self._api = f"{self._web}/api"

    def _request(self, **kwargs) -> dict:
        params = kwargs.get("params", {})
        params["token"] = self._token

        r = self._session.request(
            method=kwargs.get("method", "GET").upper(),
            url=kwargs.get("url", self._api),
            params=params,
            data=kwargs.get("data", None),
            headers=kwargs.get("headers", Client.HEADERS))
        content = r.json()
        code = content.get("statusCode", 1)
        if not r.ok or (code != 0 and code != 39):
            raise Exception(r.text)
        return content.get("data", None) or content

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
                raise Exception("Invalid password/login")
        elif token is not None:
            self._token = token
        elif xfss is not None:
            self._session.cookies.set("xfss", xfss)
        else:
            raise Exception("Invalid login credentials")

        if token is None:
            r = self._session.request(method="GET", url=f"{self._web}/my_account")
            soup = BeautifulSoup(r.content, "html.parser")
            content_wrapper_div = soup.find("div", {"id": "content-wrapper"})
            data_ui = json.loads(content_wrapper_div.select_one('.width-content')['data-ui'])
            self._token = data_ui["token"]
        return self.get_user()

    def get_user(self) -> dict:
        return self._request(url=f"{self._api}/user/me")

    def get_file_info(self, code: str) -> dict:
        data = self._request(url=f"{self._api}/link/info", params={"fileCodes": get_code(code)})["list"][0]
        data["file_size"] = get_size(data["file_size"])
        return data

    def file_search(self, path: str, search: str, limit: int = 10) -> dict:
        return self._request(url=f"{self._api}/user/files", params={
            "path": path,
            "limit": limit,
            "searchField": "file_name",
            "search": search
        })

    def get_link(self, code: str):
        code = get_code(code)
        data = self._request(url=f"{self._api}/link", params={"file_code": code})
        link = data.get("dlLink", None)
        if link is None:
            waiting_time = data["waiting"] + 1
            waiting_token = data["waitingToken"]
            print(f"W: You have to wait {waiting_time} seconds to generate a new link")
            if not get_input_bool(message="Do you want to wait?", default=True):
                raise PremiumRequired("Free account, you have to wait before you can generate a new link.")
            countdown(waiting_time)
            link = self._request(url=f"{self._api}/link", params={"file_code": code, "waiting_token": waiting_token})["dlLink"]
        return link

    def upload(self, file: Path) -> dict:
        multi = MultipartEncoder(fields={"files": (file.name, open(file, "rb"))})
        headers = Client.HEADERS.copy()
        headers["content-type"] = multi.content_type
        return self._request(
            method="POST",
            url=self._request(url=f"{self._api}/upload")["uploadLink"],
            data=multi,
            headers=headers
        )["files"]
