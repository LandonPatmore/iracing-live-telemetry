from dataclasses import dataclass
from typing import List


@dataclass
class StreamableRaceInfo:
    carClassPosition: int # Streaming (websocket)
    intervalBehindLeader: float  # Streaming (websocket) TODO: Figure out how to get time behind (interval)
    percentageAroundTrack: float  # Streaming (websocket)
    onPitRoad: bool  # Streaming (websocket)
    position: int  # Streaming (websocket)
    onTrackStatus: int  # Streaming (websocket)
    relativeFromCurrentPlayer: float
