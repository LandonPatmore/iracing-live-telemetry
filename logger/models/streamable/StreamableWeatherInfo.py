from dataclasses import dataclass


@dataclass
class StreamableWeatherInfo:
    airTemp: float
    trackTemp: float
    windDirection: float
    windVelocity: float
