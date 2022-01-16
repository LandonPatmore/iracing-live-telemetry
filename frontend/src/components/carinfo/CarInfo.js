import React from "react"
import "./CarInfo.scss"
import {Stage, Layer, Rect} from "react-konva";


class CarInfo extends React.Component {
    constructor(props) {
        super(props);

        this.state = {}
    }

    render() {
        return (
            <div>
                <h4>Cars in Proximity: {this.props.carInfo.carsInProximity}</h4>
                <h4>Fuel User per Hour: {this.props.carInfo.fuelUsePerHour}</h4>
                <h4>Fuel Level: {this.props.carInfo.fuelLevel.toFixed(1)}</h4>
                <Stage width={100} height={100}>
                    <Layer>
                        <Rect
                            x={60}
                            y={100}
                            width={20}
                            scaleY={-1}
                            height={this.props.carInfo.fuelPercentage * 100}
                            fill="orange"/>
                    </Layer>
                </Stage>
            </div>
        )
    }
}

export default CarInfo;
