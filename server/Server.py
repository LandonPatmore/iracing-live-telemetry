from flask import Flask, request, jsonify
import jsons

from classes.CarInfo import CarInfo
from classes.CompetitorInfo import CompetitorInfo
from classes.GeneralInfo import GeneralInfo
from classes.RaceInfo import RaceInfo
from classes.SessionInfo import SessionInfo
from classes.TelemetryInfo import TelemetryInfo
from classes.WeatherInfo import WeatherInfo
from server.InfluxHandler import push_to_db
from server.ServerDataUtils import general_info_scrub, filter_pace_car

app = Flask(__name__)


@app.route('/status', methods=['GET'])
def status():
    return jsonify(online=True)


@app.route('/telemetry', methods=['POST'])
def telemetry_gathering():
    request_json = jsons.loads(request.json)
    push_to_db(TelemetryInfo(
        sessionId=request_json['sessionId'],
        tick=request_json['tick'],
        carInfo=CarInfo(**request_json['carInfo']),
        competitorInfo=list(
            map(lambda competitor: CompetitorInfo(**competitor), filter_pace_car(request_json['competitorInfo']))),
        generalInfo=GeneralInfo(**general_info_scrub(request_json['generalInfo'])),
        raceInfo=RaceInfo(**request_json['raceInfo']),
        sessionInfo=SessionInfo(**request_json['sessionInfo']),
        weatherInfo=WeatherInfo(**request_json['weatherInfo'])
    ))
    return jsonify(success=True)


if __name__ == '__main__':
    app.run()
