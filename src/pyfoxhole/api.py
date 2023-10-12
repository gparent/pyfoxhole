from __future__ import annotations

from requests import get

from .models import MapDataResponse, WarReportResponse, WarResponse

LIVE_API_URL = "https://war-service-live.foxholeservices.com/api"
LIVE2_API_URL = "https://war-service-live-2.foxholeservices.com/api"


class Api:
    def __init__(
        self, api_url: str | None, api_endpoint: str, timeout: int | None = 15
    ):
        self.api_base_url = LIVE_API_URL if api_url is None else api_url
        self.api_endpoint = api_endpoint
        self.timeout = timeout

    def _api_request(self, endpoint: str):
        url = f"{self.api_base_url}/{self.api_endpoint}/{endpoint}"
        response_json = get(url, timeout=self.timeout).json()
        return response_json


class WorldConquestApi(Api):
    def __init__(self, api_url: str | None, timeout: int | None = 15):
        self.api_endpoint = "worldconquest"
        super().__init__(
            api_url=api_url, api_endpoint=self.api_endpoint, timeout=timeout
        )

    def maps(self) -> list[str]:
        return self._api_request("maps")

    def maps_dynamic_public(self, map_name: str) -> MapDataResponse:
        endpoint = f"maps/{map_name}/dynamic/public"
        return self._api_request(endpoint)

    def maps_static(self, map_name: str) -> MapDataResponse:
        endpoint = f"maps/{map_name}/static"
        return self._api_request(endpoint)

    def war(self) -> WarResponse:
        return self._api_request("war")

    def war_report(self, map_name: str) -> WarReportResponse:
        endpoint = f"warReport/{map_name}"
        return self._api_request(endpoint)
