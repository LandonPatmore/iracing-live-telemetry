package com.landonpatmore.handler

import kotlinx.coroutines.ExperimentalCoroutinesApi
import java.util.Collections

class ClientHandler {
  private val connections = Collections.synchronizedSet<ConnectedClient>(LinkedHashSet())

  fun addUser(client: ConnectedClient) {
    connections.add(client)
    log(client = client)
  }

  fun removeUser(client: ConnectedClient) {
    connections.remove(client)
    log(client = client, connected = false)
  }

  internal inline fun <reified T : ConnectedClient> getConnectedClients() = getListOfOpenConnections().filterIsInstance<T>()

  @OptIn(ExperimentalCoroutinesApi::class)
  private fun getListOfOpenConnections() = connections.filter {
    !it.socket.incoming.isClosedForReceive && !it.socket.outgoing.isClosedForSend
  }

  private fun log(client: ConnectedClient, connected: Boolean = true) {
    println("${
      when (client) {
        is LoggerClient -> "logger"
        is ViewerClient -> "viewer"
      }
    } has ${if (connected) "connected" else "disconnected"}")
  }
}
