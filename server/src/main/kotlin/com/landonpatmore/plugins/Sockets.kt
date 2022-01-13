package com.landonpatmore.plugins

import com.landonpatmore.handler.ClientHandler
import com.landonpatmore.handler.LoggerClient
import com.landonpatmore.handler.ViewerClient
import io.ktor.application.Application
import io.ktor.application.install
import io.ktor.http.cio.websocket.pingPeriod
import io.ktor.http.cio.websocket.timeout
import io.ktor.routing.routing
import io.ktor.websocket.WebSockets
import io.ktor.websocket.webSocket
import java.time.Duration

fun Application.configureSockets() {
  install(WebSockets) {
    pingPeriod = Duration.ofSeconds(15)
    timeout = Duration.ofSeconds(15)
    maxFrameSize = Long.MAX_VALUE
    masking = false
  }


  routing {
    val clientHandler = ClientHandler()

    webSocket("/logger") {
      val client = LoggerClient(socket = this, clientHandler = clientHandler)
      clientHandler.addUser(client)
      client.consumeMessages()
      // Connection has closed
      clientHandler.removeUser(client)
    }

    webSocket("/viewer") {
      val client = ViewerClient(socket = this, clientHandler = clientHandler)
      clientHandler.addUser(client)
      client.consumeMessages()
      clientHandler.removeUser(client)
    }
  }
}
