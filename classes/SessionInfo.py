from dataclasses import dataclass
from typing import List

"""
Info about the current state of the session.
"""


@dataclass
class SessionInfo:
    bestLapNum: List[int]
    bestLapTime: List[float]
    carClass: List[int]
    carClassPosition: List[int]
    raceTime: List[float]
    lapsCompleted: List[int]
    percentageAroundTrack: List[float]
    lastLapTime: List[float]
    onPitRoad: List[bool]
    position: List[int]
    onTrackStatus: List[int]
