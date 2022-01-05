from typing import List

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS

from classes.CarInfo import CarInfo
from classes.CompetitorInfo import CompetitorInfo
from classes.GeneralInfo import GeneralInfo
from classes.RaceInfo import RaceInfo
from classes.SessionInfo import SessionInfo
from classes.TelemetryInfo import TelemetryInfo
from classes.WeatherInfo import WeatherInfo


def push_to_db(telemetry_info: TelemetryInfo):
    # TODO: REMOVE
    token = "kb97nsKHLeEkYoUOfL5tjz7sjON01v1X04ZRqZ1Cz8PY_o4soGcV2bH2FkVuYKORBc_NAfIO_7wZEOQ7l6ELVg=="
    org = "Landon Patmore"
    bucket = "sim-data"

    print(telemetry_info)

    with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
        write_api = client.write_api(write_options=ASYNCHRONOUS)

        points = [__create_car_info_point(telemetry_info.carInfo),
                  __create_general_info_point(telemetry_info.generalInfo),
                  __create_weather_info_point(telemetry_info.weatherInfo),
                  __create_session_info_points(telemetry_info.sessionInfo)] + __create_race_info_points(
            telemetry_info.competitorInfo,
            telemetry_info.raceInfo)

        write_api.write(bucket, org, points)


def __create_car_info_point(car_info: CarInfo) -> Point:
    return Point("car_info") \
        .tag("car", "car") \
        .field("brake_input", car_info.brakeInput) \
        .field("absActivated", car_info.absActivated) \
        .field("throttleInput", car_info.throttleInput) \
        .field("rpm", car_info.rpm) \
        .field("speed", car_info.speed) \
        .field("gear", car_info.gear) \
        .field("fuelLevel", car_info.fuelLevel) \
        .field("fuelPercentage", car_info.fuelPercentage)


def __create_general_info_point(general_info: GeneralInfo) -> Point:
    return Point("general_info") \
        .tag("generaInfo", "generalInfo") \
        .field("numTurns", general_info.numTurns) \
        .field("name", general_info.name) \
        .field("trackId", general_info.trackId) \
        .field("trackConfigName", general_info.trackConfigName) \
        .field("displayUnits", general_info.displayUnits) \
        .field("pitSpeedLimit", general_info.pitSpeedLimit)


def __create_weather_info_point(weather_info: WeatherInfo) -> Point:
    return Point("weather") \
        .tag("weather", "weather") \
        .field("airTemp", weather_info.airTemp) \
        .field("trackTemp", weather_info.trackTemp) \
        .field("windVelocity", weather_info.windVelocity) \
        .field("windDirection", weather_info.windDirection)


def __create_session_info_points(session_info: SessionInfo) -> Point:
    return Point("session_info") \
        .tag("session", "session") \
        .field("sessionState", session_info.sessionState) \
        .field("sessionTimeSinceStart", session_info.sessionTimeSinceStart) \
        .field("sessionTimeTotal", session_info.sessionTimeTotal) \
        .field("sessionTimeRemaining", session_info.sessionTimeRemaining) \
        .field("sessionTimeOfDay", session_info.sessionTimeOfDay)


def __create_race_info_points(competitor_info: List[CompetitorInfo], race_info: RaceInfo) -> List[Point]:
    competitors = list()

    for index, competitor in enumerate(competitor_info):
        competitors.append(
            Point("race_info")
                .tag("teamName", competitor.teamName + " | [#" + competitor.carNumber + "]")
                .field("userName", competitor.userName)
                .field("carName", competitor.carName)
                .field("iRating", competitor.iRating)
                .field("license", competitor.license)
                .field("position", race_info.position[index])
                .field("carClassPosition", race_info.carClassPosition[index])
                .field("raceTime", race_info.raceTime[index])
                .field("carClass", race_info.carClass[index])
                .field("onPitRoad", race_info.onPitRoad[index])
                .field("bestLapNum", race_info.bestLapNum[index])
                .field("bestLapTime", race_info.bestLapTime[index])
                .field("lapsCompleted", race_info.lapsCompleted[index])
                .field("lastLapTime", race_info.lastLapTime[index])
                .field("onTrackStatus", race_info.onTrackStatus[index])
                .field("percentageAroundTrack", race_info.percentageAroundTrack[index])
        )

    return competitors
