import responses

from pyfoxhole import Faction, LIVE_API_URL, WorldConquestApi


@responses.activate
def test_war(world_conquest_api: WorldConquestApi) -> None:
    CONQUEST_START = 1694970001969
    VICTORY_TOWNS = 32
    WARID = "ef76d532-3d72-425b-b5b8-e15376f0bc5c"
    WARNO = 107
    WINNER = "NONE"

    WAR107 = {
        "warId": WARID,
        "warNumber": WARNO,
        "winner": WINNER,
        "conquestStartTime": CONQUEST_START,
        "conquestEndTime": None,
        "resistanceStartTime": None,
        "requiredVictoryTowns": VICTORY_TOWNS,
    }

    responses.get(
        f"{LIVE_API_URL}/worldconquest/war",
        json=WAR107,
    )
    war_response = world_conquest_api.war()
    assert war_response["warId"] == WARID
    assert war_response["warNumber"] == WARNO
    assert war_response["winner"] == Faction.NONE
    assert war_response["conquestStartTime"] == CONQUEST_START
    assert war_response["conquestEndTime"] is None
    assert war_response["resistanceStartTime"] is None
    assert war_response["requiredVictoryTowns"] == VICTORY_TOWNS
