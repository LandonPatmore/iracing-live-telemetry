import com.fasterxml.jackson.module.kotlin.jacksonMapperBuilder
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import io.javalin.Javalin
import io.javalin.websocket.WsContext
import utils.Client
import utils.clientMapFromInt
import java.util.concurrent.ConcurrentLinkedQueue

private val usersConnected = ConcurrentLinkedQueue<ConnectedUser>()

fun main() {
    Javalin.create().apply {
        post("telemetry") { req ->
            val request = jacksonObjectMapper().readTree(req.body())

            request.get("client_type")?.let {
                println(
                    "Pushable ${
                        when (clientMapFromInt(it.intValue())) {
                            Client.Logger -> "Logger message"
                            Client.Unknown -> "Unknown sender message"
                            Client.Viewer -> "Viewer message"
                        }
                    }"
                )
            } ?: println("bad message: ${req.body()}")
        }

        ws("/telemetry/{user-id}") { ws ->
            ws.onConnect { context ->
                println("Client connected")
                usersConnected.add(ConnectedUser(context, context.pathParam("user-id")))
                if (shouldStartSendingData()) {
                    context.send(SendableMessage(true))
                }
            }

            ws.onClose { context ->
                usersConnected.removeIf { user ->
                    user.webSocketContext == context
                }
                usersConnected.firstOrNull { user ->
                    user.webSocketContext.session.isOpen
                }?.webSocketContext?.send(true)
            }

            ws.onMessage { message ->
                val request = jacksonObjectMapper().readTree(message.message())

                request.get("client_type")?.let {
                    println(
                        "Streamable ${
                            when (clientMapFromInt(it.intValue())) {
                                Client.Logger -> "Logger message"
                                Client.Unknown -> "Unknown sender message"
                                Client.Viewer -> "Viewer message"
                            }
                        }"
                    )
                } ?: println("bad message: ${message.message()}")
            }
        }
    }.start(7000)
}

private fun shouldStartSendingData(): Boolean = usersConnected.size == 1

private data class SendableMessage(val send: Boolean)

private data class ConnectedUser(
    val webSocketContext: WsContext,
    val userId: String
)