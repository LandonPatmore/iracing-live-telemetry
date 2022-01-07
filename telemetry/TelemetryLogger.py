import time
import irsdk
import jsons

from TelemetryDataUtils import (
    get_pushable_race_info,
    get_streamable_player_car_info,
    get_streamable_weather_info,
    get_pushable_competitor_info,
    get_pushable_general_info,
    get_streamable_race_info,
    get_streamable_session_info
)
import threading

from telemetry.WebSocketHandler import WebSocketHandler
from telemetry.models.Message import Message
from telemetry.models.MessageTypes import TELEMETRY
from telemetry.models.State import State
from telemetry.models.pushable.PushableAggregator import PushableAggregator
from telemetry.models.streamable.StreamableAggregator import StreamableAggregator


class TelemetryLogger(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        self.state = State()
        self.ir = irsdk.IRSDK()
        self.should_run = True
        # self.websocket_handler = websocket_handler

    def run(self):
        while self.should_run:
            self.is_sim_running()
            if self.state.ir_connected:
                self.get_iracing_data()
                # self.websocket_handler.send_data(jsons.dumps(Message(type=TELEMETRY, data=data)))
                # time.sleep(0.1)  # Real
                time.sleep(1)

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

    def get_iracing_data(self):
        # data per tick since data can change midway
        self.ir.freeze_var_buffer_latest()

        pushable = PushableAggregator(
            competitorInfo=get_pushable_competitor_info(self.ir),
            generalInfo=get_pushable_general_info(self.ir),
            raceInfo=get_pushable_race_info(self.ir)
        )

        # print(jsons.dumps(pushable))

        streamable = StreamableAggregator(
            playerCarInfo=get_streamable_player_car_info(self.ir),
            raceInfo=get_streamable_race_info(self.ir),
            sessionInfo=get_streamable_session_info(self.ir),
            weatherInfo=get_streamable_weather_info(self.ir)
        )

        # print("====================================================")
        #
        print(jsons.dumps(streamable))
