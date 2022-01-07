from dataclasses import dataclass


@dataclass
class StreamableRaceInfo:
    carClassPosition: int
    intervalBehindLeader: float
    percentageAroundTrack: float
    onPitRoad: bool
    position: int
    onTrackStatus: int
    relativeFromCurrentPlayer: float
