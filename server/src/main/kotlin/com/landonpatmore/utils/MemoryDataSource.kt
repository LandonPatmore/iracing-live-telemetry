package com.landonpatmore.utils

import com.landonpatmore.models.logger.LoggerGeneral
import com.landonpatmore.models.viewer.update.CarUpdate
import com.landonpatmore.models.viewer.update.CompetitorsUpdate
import com.landonpatmore.models.viewer.update.RacersUpdate


class MemoryDataSource : DataSource {
  private var car: CarUpdate? = null
  private var general: LoggerGeneral? = null
  private var competitors: CompetitorsUpdate? = null
  private var racers: RacersUpdate? = null

  fun t() {}

  override fun getLatestCar(): CarUpdate? = car

  override fun getLatestGeneral(): LoggerGeneral? = general

  override fun getLatestCompetitors(): CompetitorsUpdate? = competitors

  override fun getLatestRacers(): RacersUpdate? = racers

  override fun setLatestCar(car: CarUpdate): CarUpdate {
    this.car = car
    return car
  }

  override fun setLatestGeneral(general: LoggerGeneral): LoggerGeneral {
    this.general = general
    return general
  }

  override fun setLatestCompetitors(competitors: CompetitorsUpdate): CompetitorsUpdate {
    this.competitors = competitors
    return competitors
  }

  override fun setLatestRacers(racers: RacersUpdate): RacersUpdate {
    this.racers = racers
    return racers
  }
}
