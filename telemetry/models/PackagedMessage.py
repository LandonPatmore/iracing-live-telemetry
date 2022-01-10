from dataclasses import dataclass
from typing import Any


@dataclass
class PackagedMessage:
    message_type: int
    data: Any = object()
    client_type: int = 0
