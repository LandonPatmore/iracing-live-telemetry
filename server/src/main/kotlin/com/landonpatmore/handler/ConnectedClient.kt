package com.landonpatmore.handler

import io.ktor.http.cio.websocket.DefaultWebSocketSession

sealed interface IncomingMessageHandler {
  suspend fun consumeMessages()
}

sealed class ConnectedClient(open val socket: DefaultWebSocketSession) : IncomingMessageHandler
