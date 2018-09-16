
/* global google */

import React from "react"
import { compose, withProps, lifecycle } from "recompose"
import { withScriptjs, withGoogleMap, GoogleMap, DirectionsRenderer, Polyline, Marker } from "react-google-maps"
import { geolocated } from 'react-geolocated'
import axios from 'axios'

const MapWrapper = compose(
  withProps({
    googleMapURL: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyDYwXTA0EicoZg4cvLkEfCG-L_KRo2azCI",
    loadingElement: <div style={{ height: `100%` }} />,
    containerElement: <div style={{ height: `100%` }} />,
    mapElement: <div style={{ height: `100%` }} />,
  }), withScriptjs, withGoogleMap, lifecycle({
    componentDidMount() {
      const DirectionsService = new google.maps.DirectionsService();
      this.setState({ directions: [] })
      console.log(this.props.routes)
      for(var route of this.props.routes) {
      DirectionsService.route({
        origin: new google.maps.LatLng(route[0].lat, route[0].lng),
        destination: new google.maps.LatLng(route[route.length - 1].lat, route[route.length - 1].lng),
        travelMode: google.maps.TravelMode.DRIVING,
      }, (result, status) => {
        if (status === google.maps.DirectionsStatus.OK) {
          let directions = this.state.directions
          directions.push(result)
          this.setState({
            directions,
          });
        } else {
          console.error(`error fetching directions ${result}`);
        }
      });
        for(var index in route) {
          this.props.points.push({location: {lng: route[index].lng,  lat: route[index].lat}})
          if(index == 0)
            continue
            console.log(route[index].lat + " " + route[index].lng + " " + route[index - 1].lat + " " + route[index - 1].lng)

          DirectionsService.route({
            origin: new google.maps.LatLng(route[index].lat, route[index].lng),
            destination: new google.maps.LatLng(route[index-1].lat, route[index-1].lng),
            travelMode: google.maps.TravelMode.DRIVING,
          }, (result, status) => {
            if (status === google.maps.DirectionsStatus.OK) {
              let directions = this.state.directions
              directions.push(result)
              this.setState({
                directions,
              });
            } else {
              console.error(`error fetching directions ${result}`);
            }
          });
      }
      }
    }
  }))((props) => {
  let directions = null
  if(props.directions)
    directions = props.directions.map((direction) => { return ( <DirectionsRenderer directions={ direction } />)})
  let markers = props.points.map((point) => <Marker position={{lng: point.location.lng, lat: point.location.lat}} />)
  return(<GoogleMap defaultZoom={15} defaultCenter={{ lat: props.startLat, lng: props.startLng }}>
    { markers }
    { directions }
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
        <MapWrapper key={this.props.routes.length} routes={this.props.routes} points={this.props.points} startLat={startLat} startLng={startLng} />
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
