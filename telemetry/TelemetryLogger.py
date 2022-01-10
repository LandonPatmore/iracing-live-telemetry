import asyncio
from asyncio import Queue

import irsdk

from TelemetryDataUtils import (
    get_pushable_race_info,
    get_streamable_player_car_info,
    get_streamable_weather_info,
    get_pushable_competitor_info,
    get_pushable_general_info,
    get_streamable_race_info,
    get_streamable_session_info
)

from telemetry.models.State import State
from telemetry.models.pushable.PushableAggregator import PushableAggregator
from telemetry.models.streamable.StreamableAggregator import StreamableAggregator


class TelemetryLogger:
    def __init__(self, receiver_queue: Queue, pushable_queue: Queue, streaming_queue: Queue):
        self.state = State()
        self.ir = irsdk.IRSDK()
        self.should_run = True
        self.receiver_queue = receiver_queue
        self.pushable_queue = pushable_queue
        self.streaming_queue = streaming_queue

    async def run(self):
        # TODO: Fix this
        while True:
            self.should_run = await self.receiver_queue.get()
            if self.should_run:
                break

        while self.should_run:
            self.is_sim_running()
            if self.state.ir_connected:
                await self.get_iracing_data()
                await asyncio.sleep(5)
                # time.sleep(0.1)  # Real
                # TODO: Figure out how to shut off if told too
            # if self.receiver_queue.empty():
            #     continue
            # else:
            #     self.should_run = await self.receiver_queue.get()
            #     self.receiver_queue.task_done()

    def is_sim_running(self):
        if self.state.ir_connected and not (self.ir.is_initialized and self.ir.is_connected):
            self.state.ir_connected = False
            # don"t forget to reset your State variables
            self.state.last_car_setup_tick = -1
            # we are shutting down ir library (clearing all internal variables)
            self.ir.shutdown()
            print("irsdk disconnected")
        elif not self.state.ir_connected and self.ir.startup(
                test_file="../data/data.bin") and self.ir.is_initialized and self.ir.is_connected:
            self.state.ir_connected = True
            print("irsdk connected")

    async def get_iracing_data(self):
        # data per tick since data can change midway
        self.ir.freeze_var_buffer_latest()

        streamable = StreamableAggregator(
            playerCarInfo=get_streamable_player_car_info(self.ir),
            raceInfo=get_streamable_race_info(self.ir),
            sessionInfo=get_streamable_session_info(self.ir),
            weatherInfo=get_streamable_weather_info(self.ir)
        )

        pushable = PushableAggregator(
            competitorInfo=get_pushable_competitor_info(self.ir),
            generalInfo=get_pushable_general_info(self.ir),
            raceInfo=get_pushable_race_info(self.ir)
        )

        await self.streaming_queue.put(streamable)
        await self.pushable_queue.put(pushable)
