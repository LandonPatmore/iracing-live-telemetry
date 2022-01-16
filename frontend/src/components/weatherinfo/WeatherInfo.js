import React from "react"
import "./WeatherInfo.scss"
import {Stage, Layer, Rect, Circle, Text, Group, Arrow} from "react-konva";


class WeatherInfo extends React.Component {
    constructor(props) {
        super(props);

        this.state = {}
    }

    render() {
        let windVelocity = (this.props.weatherInfo.windDirection * 180 / Math.PI).toFixed(0)
        return (<div>
            <h2>Weather Info</h2>
            <p>Air Temp: {this.props.weatherInfo.airTemp.toFixed(1)}</p>
            <p>Track Temp: {this.props.weatherInfo.trackTemp.toFixed(1)}</p>
            <p>Wind Direction: {windVelocity}</p>
            <p>Wind Velocity: {this.props.weatherInfo.windVelocity.toFixed(1)} m/s</p>

            <div style={{display: "inline-block"}}>
                <Stage width={100} height={100} style={{transform: `rotate(${windVelocity}deg)`}}>
                    <Layer>
                        <Arrow
                            points={[50, 100, 50, 50]}
                            centeredScaling={true}
                            pointerLength={10}
                            pointerWidth={10}
                            fill={'black'}
                            stroke={'black'}
                            strokeWidth={4}
                        />
                    </Layer>
                </Stage>
            </div>
        </div>)
    }
}

export default WeatherInfo;
