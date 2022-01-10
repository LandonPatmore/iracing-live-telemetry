package models.streamable

data class StreamableSessionInfo(
    val sessionTimeOfDay: Float,
    val sessionTimeRemaining: Float,
    val sessionTimeTotal: Float
)
