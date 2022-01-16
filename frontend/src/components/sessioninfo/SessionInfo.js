import React from "react"
import "./SessionInfo.scss"

class SessionInfo extends React.Component {
    constructor(props) {
        super(props);

        this.state = {}
    }

    generateTime(sessionTime) {
        return new Date(sessionTime * 1000).toISOString().substr(11, 8)
    }

    render() {
        return (<div>
            <h2>Session Info</h2>
            <p>Time of Day: {this.generateTime(this.props.sessionInfo.sessionTimeOfDay)}</p>
            <p>Session Time Remaining: {this.generateTime(this.props.sessionInfo.sessionTimeRemaining)}</p>
            <p>Session Time Elapsed: {this.generateTime(this.props.sessionInfo.sessionTimeTotal - this.props.sessionInfo.sessionTimeRemaining)}</p>
            <p>Session Time Total: {this.generateTime(this.props.sessionInfo.sessionTimeTotal)}</p>
        </div>)
    }
}

export default SessionInfo;
