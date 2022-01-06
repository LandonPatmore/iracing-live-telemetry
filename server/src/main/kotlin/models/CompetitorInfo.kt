package models

data class CompetitorInfo(
    val carIdx: Int,
    val userName: String,
    val userId: Int,
    val teamId: Int,
    val teamName: String,
    val carNumber: String,
    val carName: String,
    val carId: Int,
    val iRating: Int,
    val license: String,
    val licenseColor: Int
)
