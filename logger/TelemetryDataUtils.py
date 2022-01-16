import math
from typing import List
import irsdk

from models import pushable_pb2, streaming_pb2


def __getCar(ir: irsdk, info: streaming_pb2.Info):
    info.car.fuelLevel = ir["FuelLevel"]
    info.car.fuelPercentage = ir["FuelLevelPct"]
    info.car.fuelUsePerHour = ir["FuelUsePerHour"]
    info.car.lfTireWear.extend([ir["LFwearL"], ir["LFwearM"], ir["LFwearR"]])
    info.car.lrTireWear.extend([ir["LRwearL"], ir["LRwearM"], ir["LRwearR"]])
    info.car.rfTireWear.extend([ir["RFwearL"], ir["RFwearM"], ir["RFwearR"]])
    info.car.rrTireWear.extend([ir["RRwearL"], ir["RRwearM"], ir["RRwearR"]])
    info.car.lfTireTemp.extend([ir["LFtempCL"], ir["LFtempCM"], ir["LFtempCR"]])
    info.car.lrTireTemp.extend([ir["LRtempCL"], ir["LRtempCM"], ir["LRtempCR"]])
    info.car.rfTireTemp.extend([ir["RFtempCL"], ir["RFtempCM"], ir["RFtempCR"]])
    info.car.rrTireTemp.extend([ir["RRtempCL"], ir["RRtempCM"], ir["RRtempCR"]])
    info.car.tireSetsAvailable = ir["TireSetsAvailable"]
    info.car.tireSetsUsed = ir["TireSetsUsed"]
    info.car.pitServiceStatus = ir["PlayerCarPitSvStatus"]
    info.car.flagStatus = ir["SessionFlags"]
    info.car.engineWarnings = ir["EngineWarnings"]
    info.car.carsInProximity = ir["CarLeftRight"]


def __getSession(ir: irsdk, info: streaming_pb2.Info) -> streaming_pb2.Session:
    info.session.tick = ir["SessionTick"]
    info.session.timeOfDay = ir["SessionTimeOfDay"]
    info.session.timeRemaining = ir["SessionTimeRemain"]
    info.session.totalLaps = ir["SessionLapsTotal"]
    info.session.lapsRemaining = ir["SessionLapsRemainEx"]


def __getWeather(ir: irsdk, info: streaming_pb2.Info) -> streaming_pb2.Weather:
    airTemp = ir["AirTemp"]
    trackTemp = ir["TrackTempCrew"]

    def fToC(temp) -> float:
        return (temp - 32) * 5 / 9

    if ir["DisplayUnits"] == 1:
        correctedAirTemp = airTemp
        correctedTrackTemp = trackTemp
    else:
        # convert to c
        correctedAirTemp = fToC(airTemp)
        correctedTrackTemp = fToC(trackTemp)

    info.weather.airTemp = correctedAirTemp
    info.weather.trackTemp = correctedTrackTemp
    info.weather.windDirection = ir["WindDir"]
    info.weather.windVelocity = ir["WindVel"]


def __getCompetitors(ir: irsdk, info: streaming_pb2.Info):
    carIdxs: List[int] = list(map(lambda driver: driver["CarIdx"], ir["DriverInfo"]["Drivers"]))

    for idx in carIdxs:
        competitor: streaming_pb2.Competitor = info.competitors.add()

        competitor.carIdx = idx
        competitor.carClass = ir["CarIdxClass"][idx]
        competitor.carClassPosition = ir["CarIdxClassPosition"][idx]
        competitor.intervalBehindLeader = ir["CarIdxF2Time"][idx]
        competitor.percentageAroundTrack = ir["CarIdxLapDistPct"][idx]
        competitor.onPitRoad = ir["CarIdxOnPitRoad"][idx]
        competitor.position = ir["CarIdxPosition"][idx]
        competitor.trackStatus = ir["CarIdxTrackSurface"][idx]
        competitor.bestLapNum = ir["CarIdxBestLapNum"][idx]
        competitor.bestLapTime = ir["CarIdxBestLapTime"][idx]
        competitor.lapsCompleted = ir["CarIdxLapCompleted"][idx]
        competitor.lastLapTime = ir["CarIdxLastLapTime"][idx]

        driverInfo = ir["DriverInfo"]["Drivers"][idx]

        competitor.userName = driverInfo["UserName"]
        competitor.userId = driverInfo["UserID"]

        teamId = driverInfo["TeamID"]
        if teamId != 0:
            competitor.teamId = teamId
            competitor.teamName = driverInfo["TeamName"]

        competitor.carNumber = driverInfo["CarNumber"]
        competitor.carId = driverInfo["CarID"]
        competitor.iRating = driverInfo["IRating"]
        competitor.license = driverInfo["LicString"]


def getInfo(ir: irsdk) -> streaming_pb2.Info:
    info: streaming_pb2.Info = streaming_pb2.Info()

    __getCar(ir=ir, info=info)
    __getSession(ir=ir, info=info)
    __getWeather(ir=ir, info=info)
    __getCompetitors(ir=ir, info=info)

    return info


def getGeneral(ir: irsdk) -> pushable_pb2.General:
    general: pushable_pb2.General = pushable_pb2.General()

    weekend_info = ir["WeekendInfo"]
    speedLimit = weekend_info["TrackPitSpeedLimit"]

    def ceilSpeedLimit(speed) -> float:
        return math.ceil(float(speed))

    if ir["DisplayUnits"] == 1:
        correctedSpeedLimit = ceilSpeedLimit(speedLimit.split()[0])  # 88.12 kph = 89
    else:
        # convert to kph
        correctedSpeedLimit = ceilSpeedLimit(float(speedLimit.split()[0]) * 1.609)  # 54.75 mpb = 89

    general.name = weekend_info["TrackDisplayName"]
    general.trackId = weekend_info["TrackID"]
    general.trackConfigName = weekend_info["TrackConfigName"]
    general.numTurns = weekend_info["TrackNumTurns"]
    general.pitSpeedLimit = correctedSpeedLimit
    general.sectors.extend(list(map(lambda sector: sector["SectorStartPct"], ir["SplitTimeInfo"]["Sectors"])))
    general.totalTime = ir["SessionTimeTotal"]

    return general
