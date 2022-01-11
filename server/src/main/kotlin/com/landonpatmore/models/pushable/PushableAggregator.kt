package models.pushable

data class PushableAggregator(
    val competitorInfo: List<PushableCompetitorInfo>,
    val generalInfo: PushableGeneralInfo,
    val raceInfo: List<PushableRaceInfo>
)
