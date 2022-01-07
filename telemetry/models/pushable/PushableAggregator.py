from dataclasses import dataclass
from typing import List
from telemetry.models.pushable.PushableCompetitorInfo import PushableCompetitorInfo
from telemetry.models.pushable.PushableGeneralInfo import PushableGeneralInfo
from telemetry.models.pushable.PushableRaceInfo import PushableRaceInfo


@dataclass
class PushableAggregator:
    competitorInfo: List[PushableCompetitorInfo]
    generalInfo: PushableGeneralInfo
    raceInfo: List[PushableRaceInfo]
