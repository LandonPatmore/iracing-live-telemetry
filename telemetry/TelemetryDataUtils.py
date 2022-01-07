from typing import List
import irsdk

from telemetry.models.pushable.PushableCompetitorInfo import PushableCompetitorInfo
from telemetry.models.pushable.PushableGeneralInfo import PushableGeneralInfo
from telemetry.models.pushable.PushableRaceInfo import PushableRaceInfo
from telemetry.models.streamable.StreamablePlayerCarInfo import StreamablePlayerCarInfo
from telemetry.models.streamable.StreamableRaceInfo import StreamableRaceInfo
from telemetry.models.streamable.StreamableSessionInfo import StreamableSessionInfo
from telemetry.models.streamable.StreamableWeatherInfo import StreamableWeatherInfo


def get_pushable_competitor_info(ir: irsdk) -> List[PushableCompetitorInfo]:
    drivers = ir["DriverInfo"]["Drivers"]
    return list(map(lambda driver: PushableCompetitorInfo(
        carIdx=driver["CarIdx"],
        userName=driver["UserName"],
        userId=driver["UserID"],
        teamId=driver["TeamID"],
        teamName=driver["TeamName"],
        carNumber=driver["CarNumber"],
        carName=driver["CarScreenName"],
        carId=driver["CarID"],
        iRating=driver["IRating"],
        license=driver["LicString"],
        licenseColor=driver["LicColor"]
    ), drivers))


def get_pushable_general_info(ir: irsdk) -> PushableGeneralInfo:
    weekend_info = ir["WeekendInfo"]
    return PushableGeneralInfo(
        name=weekend_info["TrackDisplayName"],
        trackId=weekend_info["TrackID"],
        trackConfigName=weekend_info["TrackConfigName"],
        numTurns=weekend_info["TrackNumTurns"],
        pitSpeedLimit=weekend_info["TrackPitSpeedLimit"],
        sectors=list(map(lambda sector: sector["SectorStartPct"], ir["SplitTimeInfo"]["Sectors"]))
    )


def get_pushable_race_info(ir: irsdk) -> PushableRaceInfo:
    return PushableRaceInfo(
        bestLapNum=ir["CarIdxBestLapNum"],
        bestLapTime=ir["CarIdxBestLapTime"],
        carClass=ir["CarIdxClass"],
        lapsCompleted=ir["CarIdxLapCompleted"],
        lastLapTime=ir["CarIdxLastLapTime"],
    )


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


def get_streamable_race_info(ir: irsdk) -> StreamableRaceInfo:
    return StreamableRaceInfo(
        carClassPosition=ir["CarIdxClassPosition"],
        intervalBehindLeader=ir["CarIdxF2Time"],
        percentageAroundTrack=ir["CarIdxLapDistPct"],
        onPitRoad=ir["CarIdxOnPitRoad"],
        position=ir["CarIdxPosition"],
        onTrackStatus=ir["CarIdxTrackSurface"],
        relativeFromCurrentPlayer=ir['CarIdxEstTime']
    )


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
