from dataclasses import dataclass

"""
Info about the current state of the session.
"""


# Time series data (tick)
@dataclass
class SessionInfo:
    sessionState: int
    sessionTimeSinceStart: float
    sessionTimeOfDay: float
    sessionTimeRemaining: float
    sessionTimeTotal: float
