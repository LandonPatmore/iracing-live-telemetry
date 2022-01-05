from typing import List
import irsdk

from classes.CarInfo import CarInfo
from classes.CompetitorInfo import CompetitorInfo
from classes.GeneralInfo import GeneralInfo
from classes.RaceInfo import RaceInfo
from classes.SessionInfo import SessionInfo
from classes.WeatherInfo import WeatherInfo


def get_car_info(ir: irsdk) -> CarInfo:
    return CarInfo(
        brakeInput=ir['Brake'],
        absActivated=ir['BrakeABSactive'],
        throttleInput=ir['Throttle'],
        rpm=ir['RPM'],
        speed=ir['Speed'],
        gear=ir['Gear'],
        fuelLevel=ir['FuelLevel'],
        fuelPercentage=ir['FuelLevelPct']
    )


def get_general_info(ir: irsdk) -> GeneralInfo:
    weekend_info = ir['WeekendInfo']
    return GeneralInfo(
        name=weekend_info['TrackDisplayName'],
        trackId=weekend_info['TrackID'],
        trackConfigName=weekend_info['TrackConfigName'],
        numTurns=weekend_info['TrackNumTurns'],
        pitSpeedLimit=weekend_info['TrackPitSpeedLimit'],
        displayUnits=ir['DisplayUnits'],
        sectors=list(map(lambda sector: sector['SectorStartPct'], ir['SplitTimeInfo']['Sectors']))
    )


def get_race_info(ir: irsdk) -> RaceInfo:
    return RaceInfo(
        bestLapNum=ir['CarIdxBestLapNum'],
        bestLapTime=ir['CarIdxBestLapTime'],
        carClass=ir['CarIdxClass'],
        carClassPosition=ir['CarIdxClassPosition'],
        raceTime=ir['CarIdxF2Time'],
        lapsCompleted=ir['CarIdxLapCompleted'],
        percentageAroundTrack=ir['CarIdxLapDistPct'],
        lastLapTime=ir['CarIdxLastLapTime'],
        onPitRoad=ir['CarIdxOnPitRoad'],
        position=ir['CarIdxPosition'],
        onTrackStatus=ir['CarIdxTrackSurface']
    )


def get_session_info(ir: irsdk) -> SessionInfo:
    return SessionInfo(
        sessionState=ir['SessionState'],
        sessionTimeSinceStart=ir['SessionTime'],
        sessionTimeOfDay=ir['SessionTimeOfDay'],
        sessionTimeRemaining=ir['SessionTimeRemain'],
        sessionTimeTotal=ir['SessionTimeTotal']
    )


def get_competitors(ir: irsdk) -> List[CompetitorInfo]:
    drivers = ir['DriverInfo']['Drivers']
    return list(map(lambda driver: CompetitorInfo(
        carIdx=driver['CarIdx'],
        userName=driver['UserName'],
        userId=driver['UserID'],
        teamId=driver['TeamID'],
        teamName=driver['TeamName'],
        carNumber=driver['CarNumber'],
        carName=driver['CarScreenName'],
        carId=driver['CarID'],
        iRating=driver['IRating'],
        license=driver['LicString'],
        licenseColor=driver['LicColor']
    ), drivers))


def get_weather(ir: irsdk) -> WeatherInfo:
    return WeatherInfo(
        airTemp=ir['AirTemp'],
        trackTemp=ir['TrackTemp'],
        windDirection=ir['WindDir'],
        windVelocity=ir['WindVel']
    )
