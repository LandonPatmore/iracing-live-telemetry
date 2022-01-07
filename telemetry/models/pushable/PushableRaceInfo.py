from dataclasses import dataclass
from typing import List


@dataclass
class PushableRaceInfo:
    bestLapNum: List[int]  # Non streamable (rest api)
    bestLapTime: List[float]  # Non streamable (rest api)
    carClass: List[int]  # Non streamable (rest api)
    lapsCompleted: List[int]  # Non streamable (rest api)
    lastLapTime: List[float]  # Non streamable (rest api)
