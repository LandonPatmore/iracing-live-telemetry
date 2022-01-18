package com.landonpatmore.utils

import com.landonpatmore.models.logger.LoggerCar
import com.landonpatmore.models.logger.LoggerCompetitor
import com.landonpatmore.models.logger.LoggerGeneral
import com.landonpatmore.models.logger.LoggerInfo
import com.landonpatmore.models.viewer.stream.CarStream
import com.landonpatmore.models.viewer.stream.CompetitorStream
import com.landonpatmore.models.viewer.stream.InfoStream
import com.landonpatmore.models.viewer.update.CarUpdate
import com.landonpatmore.models.viewer.update.CompetitorUpdate
import com.landonpatmore.models.viewer.update.CompetitorsUpdate
import com.landonpatmore.models.viewer.update.RacerUpdate
import com.landonpatmore.models.viewer.update.RacersUpdate

object DataArbiter {
  private val memoryDataSource = MemoryDataSource()

  fun handleStreamableData(loggerStream: LoggerInfo?): InfoStream {
    val carStream = CarStream(
        fuelLevel = loggerStream?.car?.fuelLevel,
        fuelPercentage = loggerStream?.car?.fuelPercentage,
        fuelUsePerHour = loggerStream?.car?.fuelUsePerHour,
        flagStatus = loggerStream?.car?.flagStatus,
        engineWarnings = loggerStream?.car?.engineWarnings,
        carsInProximity = loggerStream?.car?.carsInProximity
    )

    val competitorStream = loggerStream?.competitors?.map {
      CompetitorStream(
          carIdx = it.carIdx,
          carClassPosition = it.carClassPosition,
          percentageAroundTrack = it.percentageAroundTrack,
          onPitRoad = it.onPitRoad,
          position = it.position,
          trackStatus = it.trackStatus
      )
    } ?: emptyList()

    return InfoStream(
        car = carStream,
        weather = loggerStream?.weather,
        session = loggerStream?.session,
        competitors = competitorStream
    )
  }

  fun handleGeneralUpdate(loggerGeneral: LoggerGeneral?): LoggerGeneral? {
    return if (hasGeneralUpdated(old = memoryDataSource.getLatestGeneral(), new = loggerGeneral)) {
      memoryDataSource.setLatestGeneral(general = loggerGeneral!!)
    } else {
      null
    }
  }

  fun handleUpdatableData(loggerInfo: LoggerInfo?): UpdatedData = UpdatedData(
      carUpdate = handleCarUpdate(loggerInfo?.car),
      racersUpdate = handleRacerUpdate(loggerCompetitors = loggerInfo?.competitors),
      competitorsUpdate = handleCompetitorUpdate(loggerCompetitors = loggerInfo?.competitors)
  )

  private fun handleRacerUpdate(loggerCompetitors: List<LoggerCompetitor>?): RacersUpdate? {
    val latestRacers = memoryDataSource.getLatestRacers()
    var dataSame = true
    loggerCompetitors?.forEach { loggerCompetitor ->
      latestRacers?.racers?.firstOrNull {
        it.carIdx == loggerCompetitor.carIdx
      }?.let {
        if (hasRacerUpdated(old = it, new = loggerCompetitor)) {
          dataSame = false
          return@forEach
        }
      } ?: return@forEach
    }

    return if (!dataSame) {
      return generateNewRacerList(loggerCompetitors = loggerCompetitors)
    } else {
      null
    }
  }

  private fun handleCompetitorUpdate(loggerCompetitors: List<LoggerCompetitor>?): CompetitorsUpdate? {
    val latestCompetitors = memoryDataSource.getLatestCompetitors()
    var dataSame = true
    loggerCompetitors?.forEach { loggerCompetitor ->
      latestCompetitors?.competitors?.firstOrNull {
        it.carIdx == loggerCompetitor.carIdx
      }?.let {
        if (hasCompetitorUpdated(old = it, new = loggerCompetitor)) {
          dataSame = false
          return@forEach
        }
      } ?: return@forEach
    }

    return if (!dataSame) {
      return generateNewCompetitorList(loggerCompetitors = loggerCompetitors)
    } else {
      null
    }
  }

  private fun handleCarUpdate(loggerCar: LoggerCar?): CarUpdate? {
    return if (hasCarUpdated(old = memoryDataSource.getLatestCar(), new = loggerCar)) {
      val car = CarUpdate(
          lfTireWear = loggerCar?.lfTireWear ?: emptyList(),
          lrTireWear = loggerCar?.lrTireWear ?: emptyList(),
          rfTireWear = loggerCar?.rfTireWear ?: emptyList(),
          rrTireWear = loggerCar?.rrTireWear ?: emptyList(),
          lfTireTemp = loggerCar?.lfTireTemp ?: emptyList(),
          lrTireTemp = loggerCar?.lrTireTemp ?: emptyList(),
          rfTireTemp = loggerCar?.rfTireTemp ?: emptyList(),
          rrTireTemp = loggerCar?.rrTireTemp ?: emptyList(),
          tireSetsAvailable = loggerCar?.tireSetsAvailable,
          tireSetsUsed = loggerCar?.tireSetsUsed,
          pitServiceStatus = loggerCar?.pitServiceStatus
      )

      memoryDataSource.setLatestCar(car)
    } else {
      null
    }
  }

  private fun generateNewRacerList(loggerCompetitors: List<LoggerCompetitor>?): RacersUpdate {
    val racers = RacersUpdate(racers = loggerCompetitors?.map {
      RacerUpdate(
          carIdx = it.carIdx,
          userName = it.userName,
          userId = it.userId,
          teamId = it.teamId,
          teamName = it.teamName,
          carNumber = it.carNumber,
          carId = it.carId,
          iRating = it.iRating,
          license = it.license
      )
    } ?: emptyList())

    return memoryDataSource.setLatestRacers(racers = racers)
  }

  private fun generateNewCompetitorList(loggerCompetitors: List<LoggerCompetitor>?): CompetitorsUpdate {
    val competitors = CompetitorsUpdate(loggerCompetitors?.map {
      CompetitorUpdate(
          carIdx = it.carIdx,
          bestLapNum = it.bestLapNum,
          bestLapTime = it.bestLapTime,
          lapsCompleted = it.lapsCompleted,
          lastLapTime = it.lastLapTime,
          carClassPosition = it.carClassPosition,
          position = it.position
      )
    } ?: emptyList())

    return memoryDataSource.setLatestCompetitors(competitors = competitors)
  }

  data class UpdatedData(
      val carUpdate: CarUpdate?,
      val racersUpdate: RacersUpdate?,
      val competitorsUpdate: CompetitorsUpdate?
  )
}
