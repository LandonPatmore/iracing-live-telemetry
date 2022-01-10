package models.streamable

data class StreamableAggregator(
    val playerCarInfo: StreamablePlayerCarInfo,
    val raceInfo: List<StreamableRaceInfo>,
    val sessionInfo: StreamableSessionInfo,
    val weatherInfo: StreamableWeatherInfo
)
