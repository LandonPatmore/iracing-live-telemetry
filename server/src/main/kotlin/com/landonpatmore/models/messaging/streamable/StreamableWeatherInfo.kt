package com.landonpatmore.models.messaging.streamable

data class StreamableWeatherInfo(
    val airTemp: Float,
    val trackTemp: Float,
    val windDirection: Float,
    val windVelocity: Float
)
