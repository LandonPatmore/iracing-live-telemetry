package models

data class RaceInfo(
    val bestLapNum: List<Int>,
    val bestLapTime: List<Float>,
    val carClass: List<Int>,
    val carClassPosition: List<Int>,
    val raceTime: List<Float>,
    val lapsCompleted: List<Int>,
    val percentageAroundTrack: List<Float>,
    val lastLapTime: List<Float>,
    val onPitRoad: List<Boolean>,
    val position: List<Int>,
    val onTrackStatus: List<Int>
)
