from dataclasses import dataclass
from typing import List
from logger.models.pushable.PushableCompetitorInfo import PushableCompetitorInfo
from logger.models.pushable.PushableGeneralInfo import PushableGeneralInfo
from logger.models.pushable.PushableRaceInfo import PushableRaceInfo


@dataclass
class PushableAggregator:
    competitorInfo: List[PushableCompetitorInfo]
    generalInfo: PushableGeneralInfo
    raceInfo: List[PushableRaceInfo]
