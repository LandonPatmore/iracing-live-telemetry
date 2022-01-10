package models.pushable

data class PushableCompetitorInfo(
    val carIdx: Int,
    val userName: String,
    val userId: Int,
    val teamId: Int,
    val teamName: String,
    val carNumber: String,
    val carName: String,
    val carClass: Int,
    val carId: Int,
    val iRating: Int,
    val license: String,
    val licenseColor: Int,
    val carIsPaceCar: Int
)