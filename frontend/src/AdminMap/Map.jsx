
import React from "react"
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Polyline, Marker } from "react-google-maps"
import { geolocated } from 'react-geolocated'
import axios from 'axios'

const MapWrapper = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDYwXTA0EicoZg4cvLkEfCG-L_KRo2azCI",
    key: "AIzaSyDYwXTA0EicoZg4cvLkEfCG-L_KRo2azCI",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `100%` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }), withScriptjs, withGoogleMap
)((props) => {
  let polyLines = props.routes.map((route) => <Polyline path={route} />)
  let markers = props.points.map((point) => <Marker position={{lng: point.location.lng, lat: point.location.lat}} />)
  return(<GoogleMap defaultZoom={15} defaultCenter={{ lat: props.startLat, lng: props.startLng }}>
    { polyLines }
    { markers }
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
        <MapWrapper routes={this.props.routes} points={this.props.points} startLat={startLat} startLng={startLng} />
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
