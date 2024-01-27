import pytest

from pyfoxhole import LIVE_API_URL, WorldConquestApi


@pytest.fixture
def world_conquest_api() -> WorldConquestApi:
    return WorldConquestApi(LIVE_API_URL)
