package com.landonpatmore.utils


/**
 * Pushable Messages
 */
sealed class PushableMessage {
  object Auth : PushableMessage()
  object Aggregator : PushableMessage()
  object Unknown : PushableMessage()
}

/**
 * Streamable Messages
 */
sealed class StreamableMessage {
  object Auth : StreamableMessage()
  object Aggregator : StreamableMessage()
  object Unknown : StreamableMessage()
}

fun Int.pushableMapFromInt() = when (this) {
  1000 -> PushableMessage.Auth
  1001 -> PushableMessage.Aggregator
  else -> PushableMessage.Unknown
}

fun Int.streamableMapFromInt() = when (this) {
  1100 -> StreamableMessage.Auth
  1101 -> StreamableMessage.Aggregator
  else -> StreamableMessage.Unknown
}
