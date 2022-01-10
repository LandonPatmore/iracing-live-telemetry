import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import io.javalin.Javalin
import io.javalin.websocket.WsContext
import models.TelemetryInfo
import java.util.concurrent.ConcurrentLinkedQueue

private val usersConnected = ConcurrentLinkedQueue<ConnectedUser>()

fun main() {
    Javalin.create().apply {
        post("telemetry") { req ->
            println(req.body())
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
                println(message.message())
//                println(message.message())
//                val q = jacksonObjectMapper().readValue(message.message(), ReceivedMessage::class.java)
//                println(q)
            }
        }
    }.start(7000)
}

private fun shouldStartSendingData(): Boolean = usersConnected.size == 1

private data class SendableMessage(val send: Boolean)

private data class ReceivedMessage(
    val type: Int,
    val data: TelemetryInfo
)

private data class ConnectedUser(
    val webSocketContext: WsContext,
    val userId: String
)