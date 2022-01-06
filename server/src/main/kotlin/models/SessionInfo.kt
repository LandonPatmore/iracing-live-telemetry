package models

data class SessionInfo(
    val sessionState: Int,
    val sessionTimeSinceStart: Float,
    val sessionTimeOfDay: Float,
    val sessionTimeRemaining: Float,
    val sessionTimeTotal: Float
)
