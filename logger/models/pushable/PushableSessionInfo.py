from dataclasses import dataclass
from typing import List


@dataclass
class PushableSessionInfo:
    sessionLapsRemaining: float
    sessionLapsTotal: float
    lfTire: List[float]
    rfTire: List[float]
    lrTire: List[float]
    rrTire: List[float]
    tireSetsAvailable: int
    tireSetsUsed: int
    pitServiceStatus: int
    flagStatus: int
    engineWarnings: bool
