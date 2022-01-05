import asyncio
import time
import irsdk
from TelemetryDataUtils import get_weather, get_car_info, get_competitors, get_general_info, get_race_info, \
    get_session_info
from classes.State import State
from classes.TelemetryInfo import TelemetryInfo
from telemetry.NetworkingHandler import send_data


def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        # don't forget to reset your State variables
        state.last_car_setup_tick = -1
        # we are shutting down ir library (clearing all internal variables)
        ir.shutdown()
        print('irsdk disconnected')
    elif not state.ir_connected and ir.startup(test_file='data/data.bin') and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        print('irsdk connected')


# our main loop, where we retrieve data
# and do something useful with it
def loop():
    # data per tick since data can change midway
    ir.freeze_var_buffer_latest()

    t = TelemetryInfo(
        sessionId=ir['WeekendInfo']['SessionID'],
        tick=ir['SessionTick'],
        carInfo=get_car_info(ir),
        competitorInfo=get_competitors(ir),
        generalInfo=get_general_info(ir),
        raceInfo=get_race_info(ir),
        sessionInfo=get_session_info(ir),
        weatherInfo=get_weather(ir)
    )

    asyncio.run(send_data(t))


if __name__ == '__main__':
    # initializing ir and state
    ir = irsdk.IRSDK()
    state = State()

    try:
        # infinite loop
        while True:
            # check if we are connected to iracing
            check_iracing()
            # if we are, then process data
            if state.ir_connected:
                loop()
            # maximum you can use is 1/60
            # cause iracing updates data with 60 fps
            # time.sleep(0.1)  # Real
            time.sleep(1)
    except KeyboardInterrupt:
        # press ctrl+c to exit
        pass
