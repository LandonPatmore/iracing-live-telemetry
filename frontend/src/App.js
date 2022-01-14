import './App.scss';
import React from "react";
import {w3cwebsocket as W3CWebSocket} from "websocket";
import CarInfo from "./components/carinfo/CarInfo";
import ConnectionIndicator from "./components/connectionindicator/ConnectionIndicator";

const client = new W3CWebSocket("ws://192.168.86.64:7000/viewer")

class App extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            connected: false
        }
    }

    componentDidMount() {
        client.onopen = () => {
            console.log("Websocket connected")
            this.setState({connected: true})
        }
        client.onmessage = (message) => {
            this.setState({message: JSON.parse(message.data)})
            // console.log(this.state.message.data.playerCarInfo.brakeInput)
            console.log(this.state)
        }
    }

    render() {
        return (
            <div className="App">
                <ConnectionIndicator connected={this.state.connected}/>
                {/*<ConnectionList/>*/}
                <CarInfo/>
            </div>
        )
    }
}

export default App;
