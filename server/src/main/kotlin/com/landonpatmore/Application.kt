package com.landonpatmore

import com.landonpatmore.plugins.configureMonitoring
import com.landonpatmore.plugins.configureRouting
import com.landonpatmore.plugins.configureSerialization
import com.landonpatmore.plugins.configureSockets
import io.ktor.server.engine.*
import io.ktor.server.netty.*

fun main() {
  embeddedServer(Netty, port = 7000, host = "0.0.0.0") {
    configureMonitoring()
    configureRouting()
    configureSerialization()
    configureSockets()
  }.start(wait = true)
}
