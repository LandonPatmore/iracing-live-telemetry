from dataclasses import dataclass
from typing import List

from classes.CarInfo import CarInfo
from classes.CompetitorInfo import CompetitorInfo
from classes.GeneralInfo import GeneralInfo
from classes.SessionInfo import SessionInfo
from classes.WeatherInfo import WeatherInfo

"""
Aggregation model of all models that come out of the sim.
"""


@dataclass
class TelemetryInfo:
    tick: int
    carInfo: CarInfo
    competitorInfo: List[CompetitorInfo]
    generalInfo: GeneralInfo
    sessionInfo: SessionInfo
    weatherInfo: WeatherInfo
