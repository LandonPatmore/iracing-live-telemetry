from dataclasses import dataclass


@dataclass
class StreamableSessionInfo:
    sessionTimeOfDay: float
    sessionTimeRemaining: float
    sessionTimeTotal: float
