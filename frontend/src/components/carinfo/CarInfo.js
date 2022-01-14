import React from "react"
import "./CarInfo.scss"
import {Stage, Layer, Rect} from "react-konva";


class CarInfo extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            carInfo: {
                "absActivated": false,
                "brakeInput": 0.5,
                "carsInProximity": 0,
                "fuelLevel": 0,
                "fuelPercentage": 0,
                "fuelUsePerHour": 0,
                "gear": 0,
                "rpm": 300,
                "speed": 0,
                "throttleInput": .75
            }
        }
    }

    render() {
        return (
            <div>
                <h4>Rpm: {this.state.carInfo.rpm}</h4>
                <h4>Speed: {this.state.carInfo.speed}</h4>
                <h4>Gear: {this.state.carInfo.gear}</h4>
                <h4>Fuel User per Hour: {this.state.carInfo.fuelUsePerHour}</h4>
                <h4>ABS Activated: {this.state.carInfo.absActivated}</h4>
                <h4>Cars in Proximity: {this.state.carInfo.carsInProximity}</h4>
                <h4>Fuel Level: {this.state.carInfo.fuelLevel}</h4>
                <Stage width={100} height={100}>
                    <Layer>
                        <Rect
                            x={0}
                            y={100}
                            width={20}
                            scaleY={-1}
                            height={this.state.carInfo.brakeInput * 100}
                            fill="red"/>
                        <Rect
                            x={30}
                            y={100}
                            width={20}
                            scaleY={-1}
                            height={this.state.carInfo.throttleInput * 100}
                            fill="green"/>
                        <Rect
                            x={60}
                            y={100}
                            width={20}
                            scaleY={-1}
                            height={this.state.carInfo.fuelPercentage * 100}
                            fill="orange"/>
                    </Layer>
                </Stage>
            </div>
        )
    }
}

export default CarInfo;
