
import React from "react"
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"
import axios from 'axios'

const MapWrapper = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDYwXTA0EicoZg4cvLkEfCG-L_KRo2azCI",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `100%` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }), withScriptjs, withGoogleMap
)((props) =>
  <GoogleMap options={{draggable: false, zoomControl: false, scrollwheel: false, disableDoubleClickZoom: true}} defaultZoom={15} defaultCenter={{ lat: props.startLat, lng: props.startLng }}>
    <Marker position={{ lat: props.startLat, lng: props.startLng }} />
  </GoogleMap>
)

export default class Map extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      pointId: null,
      priority: 0,
      note: "",
    }
  }
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
        <MapWrapper startLat={startLat} startLng={startLng} isMarkerShown />
      </div>
    )
  }
}
