import React from 'react'
import Map from './Map'
import Form from './Form'
import { geolocated } from 'react-geolocated'

class MapPage extends React.Component {
  render() {
    return(
      <div className="container nopadding">
          <div className="row">
            <div className="col-md-8 nopadding">
              <Map coords={this.props.coords} />
            </div>
            <div className="col-md-4">
              <Form coords={this.props.coords} />
            </div>
          </div>
      </div>
    );
  }
}

export default geolocated({
  positionOptions: {
    enableHighAccuracy: false,
  },
  userDecisionTimeout: 20000,
})(MapPage)
