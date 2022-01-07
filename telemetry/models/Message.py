import typing
from dataclasses import dataclass


# Time series data (tick)
@dataclass
class Message:
    type: int
    data: 'typing.Any' = object()


def package_message(message_type: int, data) -> typing.Dict:
    return {
        "type": message_type,
        "data": data
    }
