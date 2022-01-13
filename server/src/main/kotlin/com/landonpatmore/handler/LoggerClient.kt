package com.landonpatmore.handler

import io.ktor.http.cio.websocket.CloseReason
import io.ktor.http.cio.websocket.DefaultWebSocketSession
import io.ktor.http.cio.websocket.Frame
import io.ktor.http.cio.websocket.close
import io.ktor.http.cio.websocket.readText

data class LoggerClient(
    override val socket: DefaultWebSocketSession,
    private val clientHandler: ClientHandler
) : ConnectedClient(socket), IncomingMessageHandler {
  override suspend fun consumeMessages() {
    socket.outgoing.send(Frame.Text("hi"))
    for (message in socket.incoming) {
      when (message) {
        is Frame.Text -> clientHandler.getConnectedClients<ViewerClient>().broadcast(message.readText())
        else -> socket.close(reason = CloseReason(code = CloseReason.Codes.CANNOT_ACCEPT,
            message = "message type not supported"))
      }
    }
  }
}
