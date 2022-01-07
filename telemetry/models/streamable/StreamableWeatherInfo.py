from dataclasses import dataclass


@dataclass
class StreamableWeatherInfo:
    airTemp: float  # (websocket)
    trackTemp: float  # (websocket)
    windDirection: float  # start finish (websocket)
    windVelocity: float  # start finish (websocket)
