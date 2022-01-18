package com.landonpatmore.utils

import com.landonpatmore.models.logger.LoggerGeneral
import com.landonpatmore.models.viewer.update.CarUpdate
import com.landonpatmore.models.viewer.update.CompetitorsUpdate
import com.landonpatmore.models.viewer.update.RacersUpdate

interface DataSource {
  fun getLatestCar(): CarUpdate?

  fun getLatestGeneral(): LoggerGeneral?

  fun getLatestCompetitors(): CompetitorsUpdate?

  fun getLatestRacers(): RacersUpdate?

  fun setLatestCar(car: CarUpdate): CarUpdate

  fun setLatestGeneral(general: LoggerGeneral): LoggerGeneral

  fun setLatestCompetitors(competitors: CompetitorsUpdate): CompetitorsUpdate

  fun setLatestRacers(racers: RacersUpdate): RacersUpdate
}
