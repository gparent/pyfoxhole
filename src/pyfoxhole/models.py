from __future__ import annotations

from enum import Flag, IntEnum, StrEnum, UNIQUE, verify
from typing import TypedDict


@verify(UNIQUE)
class BaseFlags(Flag):
    VictoryBase = 0x01
    BuildSite = 0x04
    Scorched = 0x10  # v0.22
    TownClaimed = 0x20  # v0.26


@verify(UNIQUE)
class Faction(StrEnum):
    NONE = "NONE"
    COLONIALS = "COLONIALS"
    WARDENS = "WARDENS"


@verify(UNIQUE)
class MapIcon(IntEnum):
    ForwardBase = 8
    Hospital = 11
    VehicleFactory = 12
    Refinery = 17
    Shipyard = 18
    EngineeringCenter = 19
    SalvageField = 20
    ComponentField = 21
    SulfurField = 23
    WorldMapTent = 24
    TravelTent = 25
    TrainingArea = 26
    Keep = 27
    ObservationTower = 28
    Fort = 29
    TroopShip = 30
    SulfurMine = 32
    StorageFacility = 33
    Factory = 34
    GarrisonStation = 35
    RocketSite = 37
    SalvageMine = 38
    ConstructionYard = 39
    ComponentMine = 40
    RelicBase = 45
    MassProductionFactory = 51
    Seaport = 52
    CoastalGun = 53
    SoulFactory = 54
    TownBase = 56
    StormCannon = 59
    IntelCenter = 60
    CoalField = 61
    OilField = 62


class MapItem(TypedDict):
    teamId: Faction
    iconType: MapIcon
    x: float
    y: float
    flags: int


class MapTextItem(TypedDict):
    text: str
    x: float
    y: float
    mapMarkerType: str


class MapDataResponse(TypedDict):
    regionId: int
    scorchedVictoryTowns: int
    mapItems: list[MapItem]
    mapItemsC: list[MapItem]
    mapItemsW: list[MapItem]
    mapTextItems: list[MapTextItem]
    lastUpdated: int
    version: int


class WarResponse(TypedDict):
    warId: str
    warNumber: int
    winner: Faction
    conquestStartTime: int
    conquestEndTIme: int
    resistanceStartTime: int
    requiredVictoryTowns: int


class WarReportResponse(TypedDict):
    totalEnlistments: int
    colonialCasualties: int
    wardenCasualties: int
    dayOfWar: int
