import asyncio
import irsdk
from asyncio import Queue

from TelemetryDataUtils import getInfo, getGeneral
from models.State import State


class TelemetryLogger:
    def __init__(self, receiver_queue: Queue, pushable_queue: Queue, streaming_queue: Queue):
        self.state = State()
        self.ir = irsdk.IRSDK()
        self.should_run = False
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
                # await asyncio.sleep(0.1)
                # TODO: Figure out how to shut off if told too

    def is_sim_running(self):
        if self.state.ir_connected and not (self.ir.is_initialized and self.ir.is_connected):
            self.state.ir_connected = False
            # don"t forget to reset your State variables
            self.state.last_car_setup_tick = -1
            # we are shutting down ir library (clearing all internal variables)
            self.ir.shutdown()
            print("irsdk disconnected")
        elif not self.state.ir_connected and self.ir.startup(test_file="./data/data.bin") and self.ir.is_initialized and self.ir.is_connected:
            self.state.ir_connected = True
            print("irsdk connected")

    async def get_iracing_data(self):
        # data per tick since data can change midway
        self.ir.freeze_var_buffer_latest()

        streamable = getInfo(self.ir)
        pushable = getGeneral(self.ir)

        print(streamable.SerializeToString())

        await self.streaming_queue.put(streamable.SerializeToString())
        # await self.pushable_queue.put(pushable.SerializeToString())
