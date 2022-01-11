package com.landonpatmore.plugins

import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.landonpatmore.models.streamable.receivable.StreamableAuthMessage
import com.landonpatmore.models.streamable.sendable.ConnectedClient
import io.ktor.application.Application
import io.ktor.application.install
import io.ktor.http.cio.websocket.CloseReason
import io.ktor.http.cio.websocket.DefaultWebSocketSession
import io.ktor.http.cio.websocket.Frame
import io.ktor.http.cio.websocket.close
import io.ktor.http.cio.websocket.pingPeriod
import io.ktor.http.cio.websocket.readText
import io.ktor.http.cio.websocket.timeout
import io.ktor.routing.routing
import io.ktor.websocket.WebSockets
import io.ktor.websocket.webSocket
import kotlinx.coroutines.ExperimentalCoroutinesApi
import java.time.Duration
import java.util.Collections

fun Application.configureSockets() {
  install(WebSockets) {
    pingPeriod = Duration.ofSeconds(15)
    timeout = Duration.ofSeconds(15)
    maxFrameSize = Long.MAX_VALUE
    masking = false
  }

  routing {
    val connections = Collections.synchronizedSet<Connection?>(LinkedHashSet())

    webSocket("/logger") {
      try {
        println("logger has connected")
        outgoing.send(Frame.Text(jacksonObjectMapper().writeValueAsString(mapOf("message_type" to 1))))
        for (message in incoming) {
          when (message) {
            is Frame.Text -> if (authenticateUser(connections = connections, frame = message, clientType = 0)) {
              connections.broadcastMessage(connections.generateListOfConnectedClients())
            }
            else -> close(CloseReason(code = CloseReason.Codes.CANNOT_ACCEPT, "message not supported: ${message.data}"))
          }
        }
      } catch (e: Exception) {
        println("Exception: ${e.message}")
      } finally {
        println("Removing client")
        println("Was client authenticated: ${
          connections.removeIf {
            it.session == this
          }
        }")
        connections.broadcastMessage(connections.generateListOfConnectedClients())
      }
    }

    webSocket("/viewer") {
      println("viewer has connected")
    }
  }
}

private suspend fun DefaultWebSocketSession.authenticateUser(
    connections: MutableSet<Connection>, frame: Frame.Text, clientType: Int
): Boolean {
  val message = frame.readText()
  return try {
    val streamableAuthMessage = jacksonObjectMapper().readValue(message, StreamableAuthMessage::class.java)
    connections.addUser(session = this, streamableAuthMessage = streamableAuthMessage, clientType = clientType)
  } catch (e: Exception) {
    close(CloseReason(code = CloseReason.Codes.CANNOT_ACCEPT, message = "auth message was invalid: $message"))
    false
  }
}

private fun MutableSet<Connection>.addUser(
    session: DefaultWebSocketSession, streamableAuthMessage: StreamableAuthMessage, clientType: Int
): Boolean {
  return add(Connection(type = clientType, userName = streamableAuthMessage.userName, session = session))
}

@OptIn(ExperimentalCoroutinesApi::class)
private suspend fun MutableSet<Connection>.generateListOfConnectedClients(): Frame.Text = Frame.Text(jacksonObjectMapper().writeValueAsString(
    this.filter { con ->
      !con.session.incoming.isClosedForReceive && !con.session.outgoing.isClosedForSend
    }.map { con ->
      ConnectedClient(type = con.type, userName = con.userName)
    }))

@OptIn(ExperimentalCoroutinesApi::class)
private suspend fun MutableSet<Connection>.broadcastMessage(frame: Frame.Text) {
  filter {
    !it.session.outgoing.isClosedForSend
  }.forEach {
    it.session.outgoing.send(frame)
  }
}

data class Connection(
    val type: Int, val userName: String, val session: DefaultWebSocketSession
)
