package com.landonpatmore

import io.ktor.server.engine.*
import io.ktor.server.netty.*
import com.landonpatmore.plugins.*

fun main() {
    embeddedServer(Netty, port = 7000, host = "0.0.0.0") {
        configureMonitoring()
        configureRouting()
        configureSerialization()
        configureSockets()
    }.start(wait = true)
}
