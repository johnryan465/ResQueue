import React from 'react'
import axios from 'axios'
import SuccessDisplay from './SuccessDisplay'

export default class Form extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      note: "",
      priority: 1,
      submitted: false,
      longitude: "",
      latitude: "",
      manualLocation: false
    }
    this.onSubmit = this.onSubmit.bind(this)
    this.onChange = this.onChange.bind(this)
    this.toggleManualLocation = this.toggleManualLocation.bind(this)
  }
  onSubmit(event) {
    let lng = this.props.coords.longitude
    if(this.state.manualLocation && this.state.longitude) {
      lng = this.state.longitude
    }
    let lat = this.props.coords.latitude
    if(this.state.manualLocation && this.state.latitude) {
      lat = this.state.latitude
    }
    console.log(lng, lat, this.state.priority, this.state.note)
    axios.post("/api/points", {
      lng,
      lat,
      priority: this.state.priority,
      note: this.state.note
    }).then(() => {
      this.setState({ submitted: true })
    })
    event.preventDefault()
  }
  onChange(event) {
    let name = event.target.name
    let value = event.target.value
    this.setState({ [name]: value })
  }
  toggleManualLocation() {
    this.setState({ manualLocation: !this.state.manualLocation })
  }
  render() {
    if(this.state.submitted) {
      return <SuccessDisplay />
    }
    return(
      <form onSubmit={this.onSubmit} className="resqueue-form">
      <h4>Need our assistance?</h4>
      <div className="form-check">
        <input onChange={this.toggleManualLocation} value={this.state.manualLocation} className="form-check-input" type="checkbox" />
        <label className="form-check-label">Would you like to enter your location manually?</label>
      </div>
        <div className="form-group" hidden={!this.state.manualLocation}>
          <label>Latitude</label>
          <input onChange={this.onChange} value={this.state.latitude} name="latitude" className="form-control" />
        </div>
        <div className="form-group" hidden={!this.state.manualLocation}>
          <label>Longitude</label>
          <input onChange={this.onChange} value={this.state.longitude} name="longitude" className="form-control" />
        </div>
        <div className="form-group">
          <label>Note</label>
          <input onChange={this.onChange} name="note" className="form-control" placeholder="Note" />
        </div>
        <div className="form-group">
          <label>What is your severity?</label>
          <div className="form-check">
            <input onChange={this.onChange} checked={this.state.priority == 1} className="form-check-input" type="radio" value={1} name="priority" />
            <label className="form-check-label">Low</label>
          </div>
          <div className="form-check">
            <input onChange={this.onChange} checked={this.state.priority == 2} className="form-check-input" type="radio" value={2} name="priority" />
            <label className="form-check-label">Medium</label>
          </div>
          <div className="form-check">
            <input onChange={this.onChange} checked={this.state.priority == 3} className="form-check-input" type="radio" value={3} name="priority" />
            <label className="form-check-label">High</label>
          </div>
        </div>
        <input type="submit" value="ResQueue Me" className="btn btn-success" />
      </form>
    )
  }
}
