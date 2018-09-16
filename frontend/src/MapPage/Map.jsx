
import React from "react"
import { compose, withProps } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, Marker } from "react-google-maps"
import { geolocated } from 'react-geolocated'
import axios from 'axios'

const MapWrapper = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `100%` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }), withScriptjs, withGoogleMap
)((props) =>
  <GoogleMap defaultZoom={15} defaultCenter={{ lat: props.startLat, lng: props.startLng }}>
    <Marker position={{ lat: props.startLat, lng: props.startLng }} />
  </GoogleMap>
)

class Map extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      pointId: null,
      priority: 0,
      note: "",
    }
  }
  componentDidUpdate() {
    axios.post("/api/points", {
      latitude: this.props.coords.latitude,
      longitude: this.props.coords.longitude,
      priority: this.state.priority,
      note: this.state.note
    }).then((resp) => {
      this.setState({
        pointId: resp.data.id
      })
    })
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

export default geolocated({
  positionOptions: {
    enableHighAccuracy: false,
  },
  userDecisionTimeout: 20000,
})(Map)
