from dataclasses import dataclass

"""
Info pertaining to a competitor in the session.
"""


@dataclass
class CompetitorInfo:
    carIdx: int
    userName: str
    userId: int
    teamId: int
    teamName: str
    carNumber: str
    carName: str
    carId: int
    iRating: int
    license: str
    licenseColor: int
