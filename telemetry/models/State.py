from dataclasses import dataclass

"""
State information about the telemetry logger.
"""


@dataclass
class State:
    ir_connected = False
    last_car_setup_tick = -1
