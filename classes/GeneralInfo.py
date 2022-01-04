from dataclasses import dataclass
from typing import List

"""
Info about the session overall. This info does not change after the first update.
"""


@dataclass
class GeneralInfo:
    name: str
    trackId: int
    trackConfigName: str
    numTurns: int
    pitSpeedLimit: str
    displayUnits: int
    sectors: List[float]
    sessionState: int
    sessionTime: float
    sessionTimeOfDay: float
    sessionTimeRemaining: float
    sessionTimeTotal: float
