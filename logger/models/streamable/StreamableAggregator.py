from dataclasses import dataclass
from typing import List
from logger.models.streamable.StreamablePlayerCarInfo import StreamablePlayerCarInfo
from logger.models.streamable.StreamableRaceInfo import StreamableRaceInfo
from logger.models.streamable.StreamableSessionInfo import StreamableSessionInfo
from logger.models.streamable.StreamableWeatherInfo import StreamableWeatherInfo


@dataclass
class StreamableAggregator:
    playerCarInfo: StreamablePlayerCarInfo
    raceInfo: List[StreamableRaceInfo]
    sessionInfo: StreamableSessionInfo
    weatherInfo: StreamableWeatherInfo
