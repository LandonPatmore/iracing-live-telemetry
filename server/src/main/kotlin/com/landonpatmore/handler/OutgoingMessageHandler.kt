package com.landonpatmore.handler

import io.ktor.http.cio.websocket.DefaultWebSocketSession
import io.ktor.http.cio.websocket.Frame
import kotlinx.coroutines.ExperimentalCoroutinesApi

suspend inline fun <reified T : ConnectedClient> List<T>.broadcast(
    message: String
) = forEach { it.socket.outgoing.send(Frame.Text(message)) }

@OptIn(ExperimentalCoroutinesApi::class)
suspend fun DefaultWebSocketSession.sendMessage(
    message: String
) = takeIf {
  !it.incoming.isClosedForReceive && !it.outgoing.isClosedForSend
}?.outgoing?.send(Frame.Text(message))
