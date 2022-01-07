import math
from typing import List
import irsdk
from telemetry.models.pushable.PushableCompetitorInfo import PushableCompetitorInfo
from telemetry.models.pushable.PushableGeneralInfo import PushableGeneralInfo
from telemetry.models.pushable.PushableRaceInfo import PushableRaceInfo
from telemetry.models.streamable.StreamablePlayerCarInfo import StreamablePlayerCarInfo
from telemetry.models.streamable.StreamableRaceInfo import StreamableRaceInfo
from telemetry.models.streamable.StreamableSessionInfo import StreamableSessionInfo
from telemetry.models.streamable.StreamableWeatherInfo import StreamableWeatherInfo


def get_drivers_list(ir: irsdk) -> List[int]:
    filtered_competitors = list(filter(lambda driver: driver["CarIsPaceCar"] != 1, ir["DriverInfo"]["Drivers"]))
    return list(map(lambda driver: driver["CarIdx"], filtered_competitors))


def get_pushable_competitor_info(ir: irsdk) -> List[PushableCompetitorInfo]:
    drivers = ir["DriverInfo"]["Drivers"]
    list_of_drivers = list()
    for car_idx in get_drivers_list(ir):
        list_of_drivers.append(PushableCompetitorInfo(
            carIdx=car_idx,
            userName=drivers[car_idx]["UserName"],
            userId=drivers[car_idx]["UserID"],
            teamId=drivers[car_idx]["TeamID"],
            teamName=drivers[car_idx]["TeamName"],
            carNumber=drivers[car_idx]["CarNumber"],
            carName=drivers[car_idx]["CarScreenName"],
            carClass=ir["CarIdxClass"][car_idx],
            carId=drivers[car_idx]["CarID"],
            iRating=drivers[car_idx]["IRating"],
            license=drivers[car_idx]["LicString"],
            licenseColor=drivers[car_idx]["LicColor"],
            carIsPaceCar=drivers[car_idx]['CarIsPaceCar']
        ))

    return list_of_drivers


def get_pushable_general_info(ir: irsdk) -> PushableGeneralInfo:
    weekend_info = ir["WeekendInfo"]
    track_speed_limit = weekend_info["TrackPitSpeedLimit"]

    if ir["DisplayUnits"] == 1:
        scrubbed_speed_limit = math.ceil(float(track_speed_limit.split()[0]))  # 88.12 kph = 89
    else:
        # convert to kph
        scrubbed_speed_limit = math.ceil(float(track_speed_limit.split()[0]) * 1.609)  # 54.75 mpb = 89

    return PushableGeneralInfo(
        name=weekend_info["TrackDisplayName"],
        trackId=weekend_info["TrackID"],
        trackConfigName=weekend_info["TrackConfigName"],
        numTurns=weekend_info["TrackNumTurns"],
        pitSpeedLimit=scrubbed_speed_limit,
        sectors=list(map(lambda sector: sector["SectorStartPct"], ir["SplitTimeInfo"]["Sectors"]))
    )


def get_pushable_race_info(ir: irsdk) -> List[PushableRaceInfo]:
    list_of_competitor_race_info = list()
    for car_idx in get_drivers_list(ir):
        list_of_competitor_race_info.append(PushableRaceInfo(
            carIdx=car_idx,
            bestLapNum=ir["CarIdxBestLapNum"][car_idx],
            bestLapTime=ir["CarIdxBestLapTime"][car_idx],
            lapsCompleted=ir["CarIdxLapCompleted"][car_idx],
            lastLapTime=ir["CarIdxLastLapTime"][car_idx],
        ))

    return list_of_competitor_race_info


def get_streamable_player_car_info(ir: irsdk) -> StreamablePlayerCarInfo:
    return StreamablePlayerCarInfo(
        brakeInput=ir["Brake"],
        absActivated=ir["BrakeABSactive"],
        throttleInput=ir["Throttle"],
        rpm=ir["RPM"],
        speed=ir["Speed"],
        gear=ir["Gear"],
        fuelLevel=ir["FuelLevel"],
        fuelPercentage=ir["FuelLevelPct"]
    )


def get_streamable_race_info(ir: irsdk) -> List[StreamableRaceInfo]:
    list_of_streamable_race_info = list()

    for car_idx in get_drivers_list(ir):
        list_of_streamable_race_info.append(StreamableRaceInfo(
            carClassPosition=ir["CarIdxClassPosition"][car_idx],
            intervalBehindLeader=ir["CarIdxF2Time"][car_idx],
            percentageAroundTrack=ir["CarIdxLapDistPct"][car_idx],
            onPitRoad=ir["CarIdxOnPitRoad"][car_idx],
            position=ir["CarIdxPosition"][car_idx],
            onTrackStatus=ir["CarIdxTrackSurface"][car_idx],
            relativeFromCurrentPlayer=ir['CarIdxEstTime'][car_idx]
        ))

    return list_of_streamable_race_info


def get_streamable_session_info(ir: irsdk) -> StreamableSessionInfo:
    return StreamableSessionInfo(
        sessionTimeOfDay=ir["SessionTimeOfDay"],
        sessionTimeRemaining=ir["SessionTimeRemain"],
        sessionTimeTotal=ir["SessionTimeTotal"]
    )


def get_streamable_weather_info(ir: irsdk) -> StreamableWeatherInfo:
    return StreamableWeatherInfo(
        airTemp=ir["AirTemp"],
        trackTemp=ir["TrackTemp"],
        windDirection=ir["WindDir"],
        windVelocity=ir["WindVel"]
    )
