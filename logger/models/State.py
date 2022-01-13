from dataclasses import dataclass


@dataclass
class State:
    ir_connected = False
    last_car_setup_tick = -1
