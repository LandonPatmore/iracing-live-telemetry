package com.landonpatmore.handler

import io.ktor.http.cio.websocket.CloseReason
import io.ktor.http.cio.websocket.DefaultWebSocketSession
import io.ktor.http.cio.websocket.Frame
import io.ktor.http.cio.websocket.close

data class ViewerClient(
    override val socket: DefaultWebSocketSession,
    private val clientHandler: ClientHandler
) : ConnectedClient(socket), IncomingMessageHandler {
  override suspend fun consumeMessages() {
    for (message in socket.incoming) {
      when (message) {
        is Frame.Text -> println("text")
        else -> socket.close(reason = CloseReason(code = CloseReason.Codes.CANNOT_ACCEPT,
            message = "message type not supported"))
      }
    }
  }

}
