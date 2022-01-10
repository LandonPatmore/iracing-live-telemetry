package models.pushable

data class PushableGeneralInfo(
    val name: String,
    val trackId: Int,
    val trackConfigName: String,
    val numTurns: Int,
    val pitSpeedLimit: Int,
    val sectors: List<Float>
)
