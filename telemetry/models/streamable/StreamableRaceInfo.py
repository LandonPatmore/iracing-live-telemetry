from dataclasses import dataclass
from typing import List


@dataclass
class StreamableRaceInfo:
    carClassPosition: List[int]  # Streaming (websocket)
    intervalBehindLeader: List[float]  # Streaming (websocket) TODO: Figure out how to get time behind (interval)
    percentageAroundTrack: List[float]  # Streaming (websocket)
    onPitRoad: List[bool]  # Streaming (websocket)
    position: List[int]  # Streaming (websocket)
    onTrackStatus: List[int]  # Streaming (websocket)
    relativeFromCurrentPlayer: List[float]
