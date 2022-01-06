from dataclasses import dataclass
from typing import List

"""
Info about the session overall. This info does not change after the first update.
"""


@dataclass
class GeneralInfo:
    # Static data
    name: str
    trackId: int
    trackConfigName: str
    numTurns: int
    pitSpeedLimit: str
    sectors: List[float]
