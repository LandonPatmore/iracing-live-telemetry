package com.landonpatmore.handler

import com.landonpatmore.models.Streaming
import io.ktor.http.cio.websocket.*

data class LoggerClient(
    override val socket: DefaultWebSocketSession,
    private val clientHandler: ClientHandler
) : ConnectedClient(socket), IncomingMessageHandler {
  override suspend fun consumeMessages() {
    socket.outgoing.send(Frame.Text("hi"))
    for (message in socket.incoming) {
      when (message) {
        is Frame.Binary -> printStreamingProto(message.readBytes())
        else -> socket.close(reason = CloseReason(code = CloseReason.Codes.CANNOT_ACCEPT,
            message = "message type not supported"))
      }
    }
  }
}
