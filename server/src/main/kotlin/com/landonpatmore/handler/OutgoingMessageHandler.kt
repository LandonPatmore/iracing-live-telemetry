package com.landonpatmore.handler
import com.landonpatmore.models.TypedMessage
import io.ktor.http.cio.websocket.DefaultWebSocketSession
import io.ktor.http.cio.websocket.Frame
import kotlinx.coroutines.ExperimentalCoroutinesApi

suspend inline fun <reified T : ConnectedClient> List<T>.broadcast(
    message: TypedMessage
) = forEach { it.socket.outgoing.send(Frame.Binary(fin = true, data = message.encode())) }

@OptIn(ExperimentalCoroutinesApi::class)
suspend fun DefaultWebSocketSession.sendMessage(
    message: TypedMessage
) = takeIf {
  !it.incoming.isClosedForReceive && !it.outgoing.isClosedForSend
}?.outgoing?.send(Frame.Binary(fin = false, data = message.encode()))
