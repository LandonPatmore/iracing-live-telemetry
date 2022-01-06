import typing
from dataclasses import dataclass


# Time series data (tick)
@dataclass
class Message:
    type: int
    data: 'typing.Any' = object()
