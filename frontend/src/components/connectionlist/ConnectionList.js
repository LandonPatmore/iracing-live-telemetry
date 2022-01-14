import React from "react"
import "./ConnectionList.scss"

class ConnectionList extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            connectedUsersList: [{type: 1, name: "Viewer 1"}, {type: 1, name: "Viewer 2"}, {type: 0, name: "Logger 1"}]
        }
    }

    render() {
        return (
            <div>
                <ul>
                    {
                        this.state.connectedUsersList.map(user => {
                            return <li>{user.name}</li>
                        })
                    }
                </ul>
            </div>
        )
    }
}


export default ConnectionList;
