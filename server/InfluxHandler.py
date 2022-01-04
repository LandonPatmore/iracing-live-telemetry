from typing import List

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS

from classes.CarInfo import CarInfo
from classes.CompetitorInfo import CompetitorInfo
from classes.GeneralInfo import GeneralInfo
from classes.SessionInfo import SessionInfo
from classes.TelemetryInfo import TelemetryInfo
from classes.WeatherInfo import WeatherInfo


def push_to_db(telemetry_info: TelemetryInfo):
    # TODO: REMOVE
    token = "kb97nsKHLeEkYoUOfL5tjz7sjON01v1X04ZRqZ1Cz8PY_o4soGcV2bH2FkVuYKORBc_NAfIO_7wZEOQ7l6ELVg=="
    org = "Landon Patmore"
    bucket = "sim-data"

    print(telemetry_info)

    with InfluxDBClient(url="http://192.168.86.64:8086", token=token, org=org) as client:
        write_api = client.write_api(write_options=ASYNCHRONOUS)

        points = [__create_car_info_point(telemetry_info.carInfo),
                  __create_general_info_point(telemetry_info.generalInfo),
                  __create_weather_info_point(telemetry_info.weatherInfo)] + __create_session_info_points(
            telemetry_info.competitorInfo,
            telemetry_info.sessionInfo)

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
        .field("pitSpeedLimit", general_info.pitSpeedLimit) \
        .field("sessionState", general_info.sessionState) \
        .field("sessionTime", general_info.sessionTime) \
        .field("sessionTimeTotal", general_info.sessionTimeTotal) \
        .field("sessionTimeRemaining", general_info.sessionTimeRemaining) \
        .field("sessionTimeOfDay", general_info.sessionTimeOfDay)


def __create_weather_info_point(weather_info: WeatherInfo) -> Point:
    return Point("weather") \
        .tag("weather", "weather") \
        .field("airTemp", weather_info.airTemp) \
        .field("trackTemp", weather_info.trackTemp) \
        .field("windVelocity", weather_info.windVelocity) \
        .field("windDirection", weather_info.windDirection)


def __create_session_info_points(competitor_info: List[CompetitorInfo], session_info: SessionInfo) -> List[Point]:
    competitors = list()

    for index, competitor in enumerate(competitor_info):
        competitors.append(
            Point("session_info")
                .tag("teamName", competitor.teamName + " | [#" + competitor.carNumber + "]")
                .field("userName", competitor.userName)
                .field("carName", competitor.carName)
                .field("iRating", competitor.iRating)
                .field("license", competitor.license)
                .field("position", session_info.position[index])
                .field("carClassPosition", session_info.carClassPosition[index])
                .field("raceTime", session_info.raceTime[index])
                .field("carClass", session_info.carClass[index])
                .field("onPitRoad", session_info.onPitRoad[index])
                .field("bestLapNum", session_info.bestLapNum[index])
                .field("bestLapTime", session_info.bestLapTime[index])
                .field("lapsCompleted", session_info.lapsCompleted[index])
                .field("lastLapTime", session_info.lastLapTime[index])
                .field("onTrackStatus", session_info.onTrackStatus[index])
                .field("percentageAroundTrack", session_info.percentageAroundTrack[index])
        )

    return competitors
