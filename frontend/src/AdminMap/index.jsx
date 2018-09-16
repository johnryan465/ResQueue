import React from 'react'
import Map from './Map'
import Form from './Form'
import axios from 'axios'

export default class AdminMap extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      routes: [],
      points: []
    }
    this.getRoutes = this.getRoutes.bind(this)
    this.getPoints = this.getPoints.bind(this)
  }

  getRoutes() {
    axios.get("/api/routes").then((resp) => {
      this.setState({ routes: resp.data })
    })
  }

  getPoints() {
    axios.get("/api/points").then((resp) => {
      this.setState({ points: resp.data })
    })
  }

  componentDidMount() {
    this.getPoints()
  }

  render() {
    return(
      <div className="container nopadding">
          <div className="row">
            <div className="col-md-8 nopadding">
              <Map routes={this.state.routes} points={this.state.points} />
            </div>
            <div className="col-md-4">
              <Form onClick={this.getRoutes} />
            </div>
          </div>
      </div>
    )
  }
}
