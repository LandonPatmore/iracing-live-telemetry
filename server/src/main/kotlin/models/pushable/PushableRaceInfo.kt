package models.pushable

data class PushableRaceInfo(
    val carIdx: Int,
    val bestLapNum: Int,
    val bestLapTime: Float,
    val lapsCompleted: Int,
    val lastLapTime: Float
)
