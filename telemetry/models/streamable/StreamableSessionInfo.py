from dataclasses import dataclass


@dataclass
class StreamableSessionInfo:
    sessionTimeOfDay: float  # (websocket)
    sessionTimeRemaining: float  # (websocket)
    sessionTimeTotal: float  # (websocket)
