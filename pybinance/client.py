from __future__ import annotations

import secrets
import requests

from pybinance.janus import Janus


class Client:
    HEADERS = {
        "accept": "*/*",
        "user-agent": "okhttp/4.10.0"
    }

    def __init__(self):
        self._saasexch = "https://api.saasexch.cc"
        self._session = requests.Session()

    def _request(self, **kwargs) -> dict:
        method = kwargs.get("method", "GET").upper()
        url = kwargs.get("url", self._saasexch)
        data = kwargs.get("data", None)
        params = kwargs.get("params", None)
        headers = kwargs.get("headers", Client.HEADERS)
        authorization = kwargs.get("authorization", None) or []

        if "JANUS" in authorization:
            janus = Janus()
            dig = janus.get_dig(method=method, url=url, params=params, data=data)
            jwt_token = janus.get_jwt(dig)
            headers["x-janus-token"] = jwt_token

        r = self._session.request(method=method, url=url, params=params, json=data, headers=headers)

        try:
            content = r.json()
        except:
            content = None
        if content is None or content.get("code", 1001) != 0 or not r.ok:
            raise Exception(r.text)
        return content

    def immed_register(self, device_id: str = None) -> dict:
        # shortly
        if device_id is None:
            device_id = secrets.token_bytes(16).hex()

        return self._request(
            method="POST",
            url=f"{self._saasexch}/bapi/fe/message/immed/register",
            data={"deviceId": device_id},
            authorization=["JANUS"]
        )
