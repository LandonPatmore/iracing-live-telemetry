from dataclasses import dataclass

"""
Info pertaining to a competitor in the session.
"""


# Non streamable data, but must be updateable as time goes on since drivers can change (rest api)
@dataclass
class PushableCompetitorInfo:
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
