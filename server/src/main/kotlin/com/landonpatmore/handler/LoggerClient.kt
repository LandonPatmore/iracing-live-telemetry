package com.landonpatmore.handler

import com.landonpatmore.models.TypedMessage
import com.landonpatmore.models.logger.LoggerGeneral
import com.landonpatmore.models.logger.LoggerInfo
import com.landonpatmore.utils.DataArbiter
import com.squareup.wire.AnyMessage
import com.squareup.wire.Message
import io.ktor.http.cio.websocket.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

data class LoggerClient(
    override val socket: DefaultWebSocketSession,
    private val clientHandler: ClientHandler,
    private val dataArbiter: DataArbiter
) : ConnectedClient(socket), IncomingMessageHandler {
  override suspend fun consumeMessages() {
    socket.outgoing.send(Frame.Text("hi"))
    for (message in socket.incoming) {
      when (message) {
        is Frame.Binary -> {
          val readMessage = message.readBytes()
          with(TypedMessage.ADAPTER.decode(readMessage)) {
            when (this.type) {
              TypedMessage.Type.LOGGER_UPDATE -> handleLoggerUpdate(general = this.message?.unpack(LoggerGeneral.ADAPTER))
              TypedMessage.Type.LOGGER_STREAM -> {
                val infoMessage = this.message?.unpack(LoggerInfo.ADAPTER)
                handleLoggerStreamable(info = infoMessage)
                handleLoggerUpdatable(info = infoMessage)
              }
              else -> socket.closeConnection()
            }
          }
        }
        else -> socket.closeConnection()
      }
    }
  }

  private suspend fun handleLoggerUpdate(general: LoggerGeneral?) {
    val newGeneral = dataArbiter.handleGeneralUpdate(loggerGeneral = general)

    newGeneral?.let {
      sendMessage(type = TypedMessage.Type.VIEWER_GENERAL_UPDATE, data = it)
    }
  }

  private suspend fun handleLoggerStreamable(info: LoggerInfo?) {
    sendMessage(type = TypedMessage.Type.VIEWER_STREAM, data = dataArbiter.handleStreamableData(info))
  }

  private suspend fun handleLoggerUpdatable(info: LoggerInfo?) {
    val updateData = dataArbiter.handleUpdatableData(loggerInfo = info)

    updateData.carUpdate?.let {
      sendMessage(type = TypedMessage.Type.VIEWER_CAR_UPDATE, data = it)
    }

    updateData.racersUpdate?.let {
      sendMessage(type = TypedMessage.Type.VIEWER_RACERS_UPDATE, data = it)
    }

    updateData.competitorsUpdate?.let {
      sendMessage(type = TypedMessage.Type.VIEWER_COMPETITORS_UPDATE, data = it)
    }
  }

  private suspend fun sendMessage(type: TypedMessage.Type, data: Message<*, *>) {
    clientHandler.getConnectedClients<ViewerClient>()
        .broadcast(TypedMessage(type = type, message = AnyMessage.pack(data)))
  }

  private suspend fun DefaultWebSocketSession.closeConnection() {
    close(reason = CloseReason(code = CloseReason.Codes.CANNOT_ACCEPT,
        message = "message type not supported"))
  }
}
