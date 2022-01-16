package com.landonpatmore.handler

import com.landonpatmore.models.Streaming

fun printStreamingProto(bytes: ByteArray) {
  with(Streaming.Info.newBuilder().mergeFrom(bytes)) {
    println(this.session)
    println(this.weather)
    println(this.car)
    println(this.competitorsList)
  }
}
