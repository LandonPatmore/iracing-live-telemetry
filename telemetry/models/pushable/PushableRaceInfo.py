from dataclasses import dataclass
from typing import List


@dataclass
class PushableRaceInfo:
    carIdx: int
    bestLapNum: int  # Non streamable (rest api)
    bestLapTime: float  # Non streamable (rest api)
    lapsCompleted: int  # Non streamable (rest api)
    lastLapTime: float  # Non streamable (rest api)
