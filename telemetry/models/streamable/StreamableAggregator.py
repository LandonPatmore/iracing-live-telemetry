from dataclasses import dataclass
from typing import List
from telemetry.models.streamable.StreamablePlayerCarInfo import StreamablePlayerCarInfo
from telemetry.models.streamable.StreamableRaceInfo import StreamableRaceInfo
from telemetry.models.streamable.StreamableSessionInfo import StreamableSessionInfo
from telemetry.models.streamable.StreamableWeatherInfo import StreamableWeatherInfo


@dataclass
class StreamableAggregator:
    playerCarInfo: StreamablePlayerCarInfo
    raceInfo: List[StreamableRaceInfo]
    sessionInfo: StreamableSessionInfo
    weatherInfo: StreamableWeatherInfo
