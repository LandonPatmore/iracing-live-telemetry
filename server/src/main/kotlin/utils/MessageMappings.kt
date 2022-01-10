package utils

/**
 * Clients
 */
sealed class Client {
    object Logger : Client()
    object Viewer : Client()
    object Unknown : Client()
}

/**
 * Pushable Messages
 */
sealed class PushableMessage {
    object Aggregator : PushableMessage()
    object Unknown : PushableMessage()
}

/**
 * Streamable Messages
 */
sealed class StreamableMessage {
    object Aggregator : StreamableMessage()
    object Unknown : StreamableMessage()
}

fun clientMapFromInt(messageType: Int) = when (messageType) {
    0 -> Client.Logger
    1 -> Client.Viewer
    else -> Client.Unknown
}

fun pushableMapFromInt(messageType: Int) = when (messageType) {
    0 -> PushableMessage.Aggregator
    else -> PushableMessage.Unknown
}

fun streamableMapFromInt(messageType: Int) = when (messageType) {
    0 -> StreamableMessage.Aggregator
    else -> StreamableMessage.Unknown
}