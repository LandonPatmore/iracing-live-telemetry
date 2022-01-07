from dataclasses import dataclass

"""
Info about the car of the user.
"""


# Streaming data (websocket)
@dataclass
class StreamablePlayerCarInfo:
    brakeInput: float
    absActivated: bool
    throttleInput: float
    rpm: int
    speed: float
    gear: int
    fuelLevel: float
    fuelPercentage: float
