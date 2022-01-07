from dataclasses import dataclass


@dataclass
class PushableRaceInfo:
    carIdx: int
    bestLapNum: int
    bestLapTime: float
    lapsCompleted: int
    lastLapTime: float
