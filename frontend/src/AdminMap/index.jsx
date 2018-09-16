import React from 'react'
import Map from './Map'
import Form from './Form'
import axios from 'axios'

export default class AdminMap extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      routes: []
    }
    this.getRoutes = this.getRoutes.bind(this)
  }

  getRoutes() {
    axios.get("/api/routes").then((resp) => {
      this.setState({ routes: resp.data })
    })
  }

  render() {
    return(
      <div className="container nopadding">
          <div className="row">
            <div className="col-md-8 nopadding">
              <Map routes={this.state.routes} />
            </div>
            <div className="col-md-4">
              <Form onClick={this.getRoutes} />
            </div>
          </div>
      </div>
    )
  }
}
