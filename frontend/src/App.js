import './App.scss';
import React from "react";
import {w3cwebsocket as W3CWebSocket} from "websocket";
import CarInfo from "./components/carinfo/CarInfo";
import ConnectionIndicator from "./components/connectionindicator/ConnectionIndicator";
import TrackMap from "./components/trackmap/TrackMap";
import WeatherInfo from "./components/weatherinfo/WeatherInfo";
import SessionInfo from "./components/sessioninfo/SessionInfo";

const client = new W3CWebSocket("ws://192.168.86.32:7000/viewer")

class App extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            connected: false,
            message: {
                data: {
                    playerCarIdx: 0,
                    playerCarInfo: {
                        carsInProximity: 0,
                        fuelUsePerHour: 0,
                        fuelLevel: 0
                    },
                    raceInfo: [],
                    sessionInfo: {
                        sessionTimeOfDay: 0,
                        sessionTimeRemaining: 0,
                        sessionTimeTotal: 0
                    },
                    weatherInfo: {
                        airTemp: 0,
                        trackTemp: 0,
                        windDirection: 0,
                        windVelocity: 0
                    }
                }
            }
        }
    }

    componentDidMount() {
        client.onopen = () => {
            console.log("Websocket connected")
            this.setState({connected: true})
        }
        client.onmessage = (message) => {
            this.setState({message: JSON.parse(message.data)})
        }
        client.onclose = () => {
            this.setState({connected: false})
        }
    }

    render() {
        return (
            <div className="App">
                <ConnectionIndicator connected={this.state.connected}/>
                {/*<ConnectionList/>*/}
                <CarInfo carInfo={this.state.message.data.playerCarInfo}/>
                <TrackMap driverIdx={this.state.message.data.playerCarIdx} raceInfo={this.state.message.data.raceInfo}/>
                <WeatherInfo weatherInfo={this.state.message.data.weatherInfo}/>
                <SessionInfo sessionInfo={this.state.message.data.sessionInfo}/>
            </div>
        )
    }
}

export default App;
