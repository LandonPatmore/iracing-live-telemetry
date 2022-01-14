from dataclasses import dataclass


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
    fuelUsePerHour: float
    carsInProximity: int
