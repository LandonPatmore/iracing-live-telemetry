from dataclasses import dataclass

"""
Info about the weather in the session.
"""


@dataclass
class WeatherInfo:
    airTemp: float
    trackTemp: float
    windDirection: float  # start finish
    windVelocity: float  # start finish
