from dataclasses import dataclass


@dataclass
class PushableCompetitorInfo:
    carIdx: int
    userName: str
    userId: int
    teamId: int
    teamName: str
    carNumber: str
    carName: str
    carClass: int
    carId: int
    iRating: int
    license: str
    licenseColor: int
    carIsPaceCar: int
