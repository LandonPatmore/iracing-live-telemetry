import com.google.protobuf.gradle.generateProtoTasks
import com.google.protobuf.gradle.id
import com.google.protobuf.gradle.plugins
import com.google.protobuf.gradle.protobuf
import com.google.protobuf.gradle.protoc

val ktor_version: String by project
val kotlin_version: String by project
val logback_version: String by project

plugins {
  application
  kotlin("jvm") version "1.6.10"
  id("com.google.protobuf") version "0.8.18"
}

group = "com.landonpatmore"
version = "0.0.1"
application {
  mainClass.set("com.landonpatmore.ApplicationKt")
}

repositories {
  mavenCentral()
}

sourceSets {
  main {
    proto {
      srcDir("../protobufs")
    }
  }
}

protobuf {
  protoc {
    artifact = "com.google.protobuf:protoc:3.19.3"
  }
}

dependencies {
  implementation("io.ktor:ktor-metrics:$ktor_version")
  implementation("io.ktor:ktor-server-core:$ktor_version")
  implementation("io.ktor:ktor-jackson:$ktor_version")
  implementation("io.ktor:ktor-websockets:$ktor_version")
  implementation("io.ktor:ktor-server-netty:$ktor_version")
  implementation("ch.qos.logback:logback-classic:$logback_version")
  implementation("com.google.protobuf:protobuf-kotlin:3.19.3")
  testImplementation("io.ktor:ktor-server-tests:$ktor_version")
  testImplementation("org.jetbrains.kotlin:kotlin-test-junit:$kotlin_version")
}
