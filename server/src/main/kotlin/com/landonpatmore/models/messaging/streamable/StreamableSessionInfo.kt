package com.landonpatmore.models.messaging.streamable

data class StreamableSessionInfo(
    val sessionTimeOfDay: Float,
    val sessionTimeRemaining: Float,
    val sessionTimeTotal: Float
)
