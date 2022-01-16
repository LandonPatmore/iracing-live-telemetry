import React from "react"
import "./TrackMap.scss"
import {Stage, Layer, Rect, Circle, Text, Group} from "react-konva";


class TrackMap extends React.Component {
    constructor(props) {
        super(props);

        this.state = {}
    }

    getCarColor(racer) {
        if (racer.onPitRoad) {
            return "black"
        } else if (racer.carClass === 2523) {
            return "orange"
        } else {
            return "blue"
        }
    }

    render() {
        return (<div>
            <Stage width={1000} height={50}>
                <Layer>
                    <Rect
                        width={1000}
                        height={50}
                        fill="gray"/>
                    {this.props.raceInfo.filter(r => r.percentageAroundTrack !== -1).map((racer, index) => {
                        return <Group key={index}>
                            <Circle
                                x={1000 * racer.percentageAroundTrack}
                                y={25}
                                width={20}
                                height={20}
                                fill={this.getCarColor(racer)}/>
                            <Text
                                x={1000 * racer.percentageAroundTrack - 5}
                                y={21}
                                text={racer.carClassPosition}
                                fill={"white"}
                            />
                        </Group>
                    })}
                </Layer>
            </Stage>
        </div>)
    }
}

export default TrackMap;
