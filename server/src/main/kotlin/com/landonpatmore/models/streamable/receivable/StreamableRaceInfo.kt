package com.landonpatmore.models.streamable.receivable

data class StreamableRaceInfo(
    val carClassPosition: Int,
    val intervalBehindLeader: Float,
    val percentageAroundTrack: Float,
    val onPitRoad: Boolean,
    val position: Int,
    val onTrackStatus: Int,
    val relativeFromCurrentPlayer: Float
)
