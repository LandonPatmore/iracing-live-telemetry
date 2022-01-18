val ktor_version: String by project
val kotlin_version: String by project
val logback_version: String by project

plugins {
  application
  kotlin("jvm") version "1.6.10"
  id("com.squareup.wire") version "4.0.1"
}

wire {
  sourcePath {
    srcDir("../protos")
  }

  kotlin{}
}

group = "com.landonpatmore"
version = "0.0.1"
application {
  mainClass.set("com.landonpatmore.ApplicationKt")
}

repositories {
  mavenCentral()
}

dependencies {
  implementation("io.ktor:ktor-metrics:$ktor_version")
  implementation("io.ktor:ktor-server-core:$ktor_version")
  implementation("io.ktor:ktor-jackson:$ktor_version")
  implementation("io.ktor:ktor-websockets:$ktor_version")
  implementation("io.ktor:ktor-server-netty:$ktor_version")
  implementation("ch.qos.logback:logback-classic:$logback_version")
  implementation("com.squareup.wire:wire-runtime:4.0.1")
  implementation("redis.clients:jedis:4.0.1")
  testImplementation("io.ktor:ktor-server-tests:$ktor_version")
  testImplementation("org.jetbrains.kotlin:kotlin-test-junit:$kotlin_version")
}
