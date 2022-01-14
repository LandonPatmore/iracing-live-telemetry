import React from "react"
import "./ConnectionIndication.scss"

class ConnectionIndicator extends React.Component {
    constructor(props) {
        super(props);

        this.state= {}
    }

    render() {
        console.log(this.props.connected)
        return (
            <div className="flex-container">
                <div className="flex-child">
                    <div className={`circle ${this.props.connected ? `circle-connected` : `circle-disconnected`}`}/>
                </div>
                <div className="flex-child">
                    <p>{this.props.connected ? "Connected" : "Disconnected"}</p>
                </div>
            </div>
        )
    }
}


export default ConnectionIndicator;
