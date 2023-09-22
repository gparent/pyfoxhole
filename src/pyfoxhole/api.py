from __future__ import annotations

from requests import get

from .models import MapDataResponse, WarReportResponse, WarResponse

LIVE_API_URL = "https://war-service-live.foxholeservices.com/api"
LIVE2_API_URL = "https://war-service-live-2.foxholeservices.com/api"


class WorldConquestApi:
    def __init__(self, api_url: str | None, timeout: int | None = 15):
        self.api_base_url = LIVE_API_URL if api_url is None else api_url
        self.timeout = timeout

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

    def _api_request(self, endpoint: str):
        url = self.api_base_url + "/worldconquest/" + endpoint
        response_json = get(url, timeout=self.timeout).json()
        return response_json
