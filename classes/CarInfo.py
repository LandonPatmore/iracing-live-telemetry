from dataclasses import dataclass

"""
Info about the car of the user.
"""


# Time series data (tick)
@dataclass
class CarInfo:
    brakeInput: float
    absActivated: bool
    throttleInput: float
    rpm: int
    speed: float
    gear: int
    fuelLevel: float
    fuelPercentage: float
