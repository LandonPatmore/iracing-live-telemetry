package models

data class TelemetryInfo(
//    val tick: Int,
    val competitorInfo: List<CompetitorInfo>,
    val raceInfo: RaceInfo,
    val sessionInfo: SessionInfo,
    val weatherInfo: WeatherInfo
)