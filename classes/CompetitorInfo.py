from dataclasses import dataclass

"""
Info pertaining to a competitor in the session.
"""


# Non time series data but does update periodically because of driver changes
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
