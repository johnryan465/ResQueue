
import React from "react"
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Polyline } from "react-google-maps"
import { geolocated } from 'react-geolocated'
import axios from 'axios'

const MapWrapper = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `100%` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }), withScriptjs, withGoogleMap
)((props) => {
  let polyLines = props.routes.map((route) => <Polyline path={route} />)
  return(<GoogleMap defaultZoom={15} defaultCenter={{ lat: props.startLat, lng: props.startLng }}>
    { polyLines }
  </GoogleMap>)
}
)

class Map extends React.Component {
  render() {
    let startLat = 0
    let startLng = 0
    if(this.props.coords) {
      startLat = this.props.coords.latitude
      startLng = this.props.coords.longitude
    } else {
      return null
    }
    return (
      <div className="map">
        <MapWrapper routes={this.props.routes} startLat={0} startLng={0} />
      </div>
    )
  }
}

export default geolocated({
  positionOptions: {
    enableHighAccuracy: false,
  },
  userDecisionTimeout: 20000,
})(Map)
