package com.landonpatmore.models.messaging.streamable

data class StreamableAggregator(
    val playerCarInfo: StreamablePlayerCarInfo,
    val raceInfo: List<StreamableRaceInfo>,
    val sessionInfo: StreamableSessionInfo,
    val weatherInfo: StreamableWeatherInfo
)
