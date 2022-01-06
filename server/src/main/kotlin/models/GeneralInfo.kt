package models

data class GeneralInfo(
    val name: String,
    val trackId: Int,
    val trackConfigName: String,
    val numTurns: Int,
    val pitSpeedLimit: String,
    val sectors: List<Float>
)
