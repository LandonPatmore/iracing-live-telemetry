from dataclasses import dataclass
from typing import List


@dataclass
class PushableGeneralInfo:
    name: str
    trackId: int
    trackConfigName: str
    numTurns: int
    pitSpeedLimit: int
    sectors: List[float]
