package com.landonpatmore.utils

import com.landonpatmore.models.logger.LoggerCar
import com.landonpatmore.models.logger.LoggerCompetitor
import com.landonpatmore.models.logger.LoggerGeneral
import com.landonpatmore.models.viewer.update.CarUpdate
import com.landonpatmore.models.viewer.update.CompetitorUpdate
import com.landonpatmore.models.viewer.update.RacerUpdate

fun hasCarUpdated(
    old: CarUpdate?,
    new: LoggerCar?
): Boolean = when {
  new == null -> false
  old == null -> true
  else -> !(old.lfTireWear.areEqual(new.lfTireWear) &&
      old.rrTireWear.areEqual(new.lrTireWear) &&
      old.rfTireWear.areEqual(new.rfTireWear) &&
      old.rrTireWear.areEqual(new.rrTireWear) &&
      old.lfTireTemp.areEqual(new.lfTireTemp) &&
      old.lrTireTemp.areEqual(new.lrTireTemp) &&
      old.rfTireTemp.areEqual(new.rfTireTemp) &&
      old.rrTireTemp.areEqual(new.rrTireTemp) &&
      old.tireSetsAvailable == new.tireSetsAvailable &&
      old.tireSetsUsed == new.tireSetsUsed &&
      old.pitServiceStatus == new.pitServiceStatus)
}

fun hasCompetitorUpdated(
    old: CompetitorUpdate?,
    new: LoggerCompetitor?
): Boolean = when {
  new == null -> false
  old == null -> true
  else -> !(old.carIdx == new.carIdx &&
      old.bestLapNum == new.bestLapNum &&
      old.bestLapTime == new.bestLapTime &&
      old.lapsCompleted == new.lapsCompleted &&
      old.lastLapTime == new.lastLapTime &&
      old.position == new.position &&
      old.carClassPosition == new.carClassPosition)
}

fun hasRacerUpdated(
    old: RacerUpdate?,
    new: LoggerCompetitor?
): Boolean = when {
  new == null -> false
  old == null -> true
  else -> !(old.carIdx == new.carIdx &&
      old.userName == new.userName &&
      old.userId == new.userId &&
      old.teamId == new.teamId &&
      old.teamName == new.teamName &&
      old.carNumber == new.carNumber &&
      old.carId == new.carId &&
      old.iRating == new.iRating &&
      old.license == new.license)
}

fun hasGeneralUpdated(
    old: LoggerGeneral?,
    new: LoggerGeneral?
): Boolean = when {
  new == null -> false
  old == null -> true
  else -> !(old.name == new.name &&
      old.trackId == new.trackId &&
      old.trackConfigName == new.trackConfigName &&
      old.numTurns == new.numTurns &&
      old.pitSpeedLimit == new.pitSpeedLimit &&
      old.sectors == new.sectors &&
      old.totalTime == new.totalTime)
}

private fun List<Float>?.areEqual(other: List<Float>?): Boolean = this?.containsAll(other ?: emptyList()) ?: false
