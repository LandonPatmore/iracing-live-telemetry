//Generated by the protocol buffer compiler. DO NOT EDIT!
// source: protobufs/streaming.proto

package streaming;

@kotlin.jvm.JvmSynthetic
public inline fun competitor(block: streaming.CompetitorKt.Dsl.() -> kotlin.Unit): streaming.Streaming.Competitor =
  streaming.CompetitorKt.Dsl._create(streaming.Streaming.Competitor.newBuilder()).apply { block() }._build()
public object CompetitorKt {
  @kotlin.OptIn(com.google.protobuf.kotlin.OnlyForUseByGeneratedProtoCode::class)
  @com.google.protobuf.kotlin.ProtoDslMarker
  public class Dsl private constructor(
    private val _builder: streaming.Streaming.Competitor.Builder
  ) {
    public companion object {
      @kotlin.jvm.JvmSynthetic
      @kotlin.PublishedApi
      internal fun _create(builder: streaming.Streaming.Competitor.Builder): Dsl = Dsl(builder)
    }

    @kotlin.jvm.JvmSynthetic
    @kotlin.PublishedApi
    internal fun _build(): streaming.Streaming.Competitor = _builder.build()

    /**
     * <code>optional int32 carIdx = 1;</code>
     */
    public var carIdx: kotlin.Int
      @JvmName("getCarIdx")
      get() = _builder.getCarIdx()
      @JvmName("setCarIdx")
      set(value) {
        _builder.setCarIdx(value)
      }
    /**
     * <code>optional int32 carIdx = 1;</code>
     */
    public fun clearCarIdx() {
      _builder.clearCarIdx()
    }
    /**
     * <code>optional int32 carIdx = 1;</code>
     * @return Whether the carIdx field is set.
     */
    public fun hasCarIdx(): kotlin.Boolean {
      return _builder.hasCarIdx()
    }

    /**
     * <code>optional int32 carClass = 2;</code>
     */
    public var carClass: kotlin.Int
      @JvmName("getCarClass")
      get() = _builder.getCarClass()
      @JvmName("setCarClass")
      set(value) {
        _builder.setCarClass(value)
      }
    /**
     * <code>optional int32 carClass = 2;</code>
     */
    public fun clearCarClass() {
      _builder.clearCarClass()
    }
    /**
     * <code>optional int32 carClass = 2;</code>
     * @return Whether the carClass field is set.
     */
    public fun hasCarClass(): kotlin.Boolean {
      return _builder.hasCarClass()
    }

    /**
     * <code>optional int32 carClassPosition = 3;</code>
     */
    public var carClassPosition: kotlin.Int
      @JvmName("getCarClassPosition")
      get() = _builder.getCarClassPosition()
      @JvmName("setCarClassPosition")
      set(value) {
        _builder.setCarClassPosition(value)
      }
    /**
     * <code>optional int32 carClassPosition = 3;</code>
     */
    public fun clearCarClassPosition() {
      _builder.clearCarClassPosition()
    }
    /**
     * <code>optional int32 carClassPosition = 3;</code>
     * @return Whether the carClassPosition field is set.
     */
    public fun hasCarClassPosition(): kotlin.Boolean {
      return _builder.hasCarClassPosition()
    }

    /**
     * <code>optional float intervalBehindLeader = 4;</code>
     */
    public var intervalBehindLeader: kotlin.Float
      @JvmName("getIntervalBehindLeader")
      get() = _builder.getIntervalBehindLeader()
      @JvmName("setIntervalBehindLeader")
      set(value) {
        _builder.setIntervalBehindLeader(value)
      }
    /**
     * <code>optional float intervalBehindLeader = 4;</code>
     */
    public fun clearIntervalBehindLeader() {
      _builder.clearIntervalBehindLeader()
    }
    /**
     * <code>optional float intervalBehindLeader = 4;</code>
     * @return Whether the intervalBehindLeader field is set.
     */
    public fun hasIntervalBehindLeader(): kotlin.Boolean {
      return _builder.hasIntervalBehindLeader()
    }

    /**
     * <code>optional float percentageAroundTrack = 5;</code>
     */
    public var percentageAroundTrack: kotlin.Float
      @JvmName("getPercentageAroundTrack")
      get() = _builder.getPercentageAroundTrack()
      @JvmName("setPercentageAroundTrack")
      set(value) {
        _builder.setPercentageAroundTrack(value)
      }
    /**
     * <code>optional float percentageAroundTrack = 5;</code>
     */
    public fun clearPercentageAroundTrack() {
      _builder.clearPercentageAroundTrack()
    }
    /**
     * <code>optional float percentageAroundTrack = 5;</code>
     * @return Whether the percentageAroundTrack field is set.
     */
    public fun hasPercentageAroundTrack(): kotlin.Boolean {
      return _builder.hasPercentageAroundTrack()
    }

    /**
     * <code>optional bool onPitRoad = 6;</code>
     */
    public var onPitRoad: kotlin.Boolean
      @JvmName("getOnPitRoad")
      get() = _builder.getOnPitRoad()
      @JvmName("setOnPitRoad")
      set(value) {
        _builder.setOnPitRoad(value)
      }
    /**
     * <code>optional bool onPitRoad = 6;</code>
     */
    public fun clearOnPitRoad() {
      _builder.clearOnPitRoad()
    }
    /**
     * <code>optional bool onPitRoad = 6;</code>
     * @return Whether the onPitRoad field is set.
     */
    public fun hasOnPitRoad(): kotlin.Boolean {
      return _builder.hasOnPitRoad()
    }

    /**
     * <code>optional int32 position = 7;</code>
     */
    public var position: kotlin.Int
      @JvmName("getPosition")
      get() = _builder.getPosition()
      @JvmName("setPosition")
      set(value) {
        _builder.setPosition(value)
      }
    /**
     * <code>optional int32 position = 7;</code>
     */
    public fun clearPosition() {
      _builder.clearPosition()
    }
    /**
     * <code>optional int32 position = 7;</code>
     * @return Whether the position field is set.
     */
    public fun hasPosition(): kotlin.Boolean {
      return _builder.hasPosition()
    }

    /**
     * <code>optional int32 trackStatus = 8;</code>
     */
    public var trackStatus: kotlin.Int
      @JvmName("getTrackStatus")
      get() = _builder.getTrackStatus()
      @JvmName("setTrackStatus")
      set(value) {
        _builder.setTrackStatus(value)
      }
    /**
     * <code>optional int32 trackStatus = 8;</code>
     */
    public fun clearTrackStatus() {
      _builder.clearTrackStatus()
    }
    /**
     * <code>optional int32 trackStatus = 8;</code>
     * @return Whether the trackStatus field is set.
     */
    public fun hasTrackStatus(): kotlin.Boolean {
      return _builder.hasTrackStatus()
    }

    /**
     * <code>optional int32 bestLapNum = 9;</code>
     */
    public var bestLapNum: kotlin.Int
      @JvmName("getBestLapNum")
      get() = _builder.getBestLapNum()
      @JvmName("setBestLapNum")
      set(value) {
        _builder.setBestLapNum(value)
      }
    /**
     * <code>optional int32 bestLapNum = 9;</code>
     */
    public fun clearBestLapNum() {
      _builder.clearBestLapNum()
    }
    /**
     * <code>optional int32 bestLapNum = 9;</code>
     * @return Whether the bestLapNum field is set.
     */
    public fun hasBestLapNum(): kotlin.Boolean {
      return _builder.hasBestLapNum()
    }

    /**
     * <code>optional float bestLapTime = 10;</code>
     */
    public var bestLapTime: kotlin.Float
      @JvmName("getBestLapTime")
      get() = _builder.getBestLapTime()
      @JvmName("setBestLapTime")
      set(value) {
        _builder.setBestLapTime(value)
      }
    /**
     * <code>optional float bestLapTime = 10;</code>
     */
    public fun clearBestLapTime() {
      _builder.clearBestLapTime()
    }
    /**
     * <code>optional float bestLapTime = 10;</code>
     * @return Whether the bestLapTime field is set.
     */
    public fun hasBestLapTime(): kotlin.Boolean {
      return _builder.hasBestLapTime()
    }

    /**
     * <code>optional int32 lapsCompleted = 11;</code>
     */
    public var lapsCompleted: kotlin.Int
      @JvmName("getLapsCompleted")
      get() = _builder.getLapsCompleted()
      @JvmName("setLapsCompleted")
      set(value) {
        _builder.setLapsCompleted(value)
      }
    /**
     * <code>optional int32 lapsCompleted = 11;</code>
     */
    public fun clearLapsCompleted() {
      _builder.clearLapsCompleted()
    }
    /**
     * <code>optional int32 lapsCompleted = 11;</code>
     * @return Whether the lapsCompleted field is set.
     */
    public fun hasLapsCompleted(): kotlin.Boolean {
      return _builder.hasLapsCompleted()
    }

    /**
     * <code>optional float lastLapTime = 12;</code>
     */
    public var lastLapTime: kotlin.Float
      @JvmName("getLastLapTime")
      get() = _builder.getLastLapTime()
      @JvmName("setLastLapTime")
      set(value) {
        _builder.setLastLapTime(value)
      }
    /**
     * <code>optional float lastLapTime = 12;</code>
     */
    public fun clearLastLapTime() {
      _builder.clearLastLapTime()
    }
    /**
     * <code>optional float lastLapTime = 12;</code>
     * @return Whether the lastLapTime field is set.
     */
    public fun hasLastLapTime(): kotlin.Boolean {
      return _builder.hasLastLapTime()
    }

    /**
     * <code>optional string userName = 13;</code>
     */
    public var userName: kotlin.String
      @JvmName("getUserName")
      get() = _builder.getUserName()
      @JvmName("setUserName")
      set(value) {
        _builder.setUserName(value)
      }
    /**
     * <code>optional string userName = 13;</code>
     */
    public fun clearUserName() {
      _builder.clearUserName()
    }
    /**
     * <code>optional string userName = 13;</code>
     * @return Whether the userName field is set.
     */
    public fun hasUserName(): kotlin.Boolean {
      return _builder.hasUserName()
    }

    /**
     * <code>optional int32 userId = 14;</code>
     */
    public var userId: kotlin.Int
      @JvmName("getUserId")
      get() = _builder.getUserId()
      @JvmName("setUserId")
      set(value) {
        _builder.setUserId(value)
      }
    /**
     * <code>optional int32 userId = 14;</code>
     */
    public fun clearUserId() {
      _builder.clearUserId()
    }
    /**
     * <code>optional int32 userId = 14;</code>
     * @return Whether the userId field is set.
     */
    public fun hasUserId(): kotlin.Boolean {
      return _builder.hasUserId()
    }

    /**
     * <code>optional int32 teamId = 15;</code>
     */
    public var teamId: kotlin.Int
      @JvmName("getTeamId")
      get() = _builder.getTeamId()
      @JvmName("setTeamId")
      set(value) {
        _builder.setTeamId(value)
      }
    /**
     * <code>optional int32 teamId = 15;</code>
     */
    public fun clearTeamId() {
      _builder.clearTeamId()
    }
    /**
     * <code>optional int32 teamId = 15;</code>
     * @return Whether the teamId field is set.
     */
    public fun hasTeamId(): kotlin.Boolean {
      return _builder.hasTeamId()
    }

    /**
     * <code>optional string teamName = 16;</code>
     */
    public var teamName: kotlin.String
      @JvmName("getTeamName")
      get() = _builder.getTeamName()
      @JvmName("setTeamName")
      set(value) {
        _builder.setTeamName(value)
      }
    /**
     * <code>optional string teamName = 16;</code>
     */
    public fun clearTeamName() {
      _builder.clearTeamName()
    }
    /**
     * <code>optional string teamName = 16;</code>
     * @return Whether the teamName field is set.
     */
    public fun hasTeamName(): kotlin.Boolean {
      return _builder.hasTeamName()
    }

    /**
     * <code>optional string carNumber = 17;</code>
     */
    public var carNumber: kotlin.String
      @JvmName("getCarNumber")
      get() = _builder.getCarNumber()
      @JvmName("setCarNumber")
      set(value) {
        _builder.setCarNumber(value)
      }
    /**
     * <code>optional string carNumber = 17;</code>
     */
    public fun clearCarNumber() {
      _builder.clearCarNumber()
    }
    /**
     * <code>optional string carNumber = 17;</code>
     * @return Whether the carNumber field is set.
     */
    public fun hasCarNumber(): kotlin.Boolean {
      return _builder.hasCarNumber()
    }

    /**
     * <code>optional int32 carId = 18;</code>
     */
    public var carId: kotlin.Int
      @JvmName("getCarId")
      get() = _builder.getCarId()
      @JvmName("setCarId")
      set(value) {
        _builder.setCarId(value)
      }
    /**
     * <code>optional int32 carId = 18;</code>
     */
    public fun clearCarId() {
      _builder.clearCarId()
    }
    /**
     * <code>optional int32 carId = 18;</code>
     * @return Whether the carId field is set.
     */
    public fun hasCarId(): kotlin.Boolean {
      return _builder.hasCarId()
    }

    /**
     * <code>optional int32 iRating = 19;</code>
     */
    public var iRating: kotlin.Int
      @JvmName("getIRating")
      get() = _builder.getIRating()
      @JvmName("setIRating")
      set(value) {
        _builder.setIRating(value)
      }
    /**
     * <code>optional int32 iRating = 19;</code>
     */
    public fun clearIRating() {
      _builder.clearIRating()
    }
    /**
     * <code>optional int32 iRating = 19;</code>
     * @return Whether the iRating field is set.
     */
    public fun hasIRating(): kotlin.Boolean {
      return _builder.hasIRating()
    }

    /**
     * <code>optional string license = 20;</code>
     */
    public var license: kotlin.String
      @JvmName("getLicense")
      get() = _builder.getLicense()
      @JvmName("setLicense")
      set(value) {
        _builder.setLicense(value)
      }
    /**
     * <code>optional string license = 20;</code>
     */
    public fun clearLicense() {
      _builder.clearLicense()
    }
    /**
     * <code>optional string license = 20;</code>
     * @return Whether the license field is set.
     */
    public fun hasLicense(): kotlin.Boolean {
      return _builder.hasLicense()
    }
  }
}
@kotlin.jvm.JvmSynthetic
public inline fun streaming.Streaming.Competitor.copy(block: streaming.CompetitorKt.Dsl.() -> kotlin.Unit): streaming.Streaming.Competitor =
  streaming.CompetitorKt.Dsl._create(this.toBuilder()).apply { block() }._build()
