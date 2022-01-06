package models

data class CarInfo(
    val brakeInput: Float,
    val absActivated: Boolean,
    val throttleInput: Float,
    val rpm: Int,
    val speed: Float,
    val gear: Int,
    val fuelLevel: Float,
    val fuelPercentage: Float
)
