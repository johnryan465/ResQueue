import React from 'react'
import axios from 'axios'

export default class EditVehiclePage extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      name: "",
      quantity: -1,
      size: -1
    }
    this.getVehicle = this.getVehicle.bind(this)
    this.onChange = this.onChange.bind(this)
    this.onSubmit = this.onSubmit.bind(this)
  }
  getVehicle() {
    axios.get(`/api/vehicles/${this.props.id}`).then((resp) => {
      this.setState({
        ...resp.data
      })
    })
  }
  componentDidMount() {
    this.getVehicle()
  }
  onChange(event) {
    let name = event.target.name
    let value = event.target.value
    this.setState({ [name]: value })
  }
  onSubmit(event) {
    axios.put(`/api/vehicles/${this.props.id}`, {
      ...this.state
    }).then((data) => {
      window.location = "/admin/vehicles"
    })
    event.preventDefault()
  }
  render() {
    return(
      <div className="container vehicle-edit-page">
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Name</label>
            <input onChange={this.onChange} className="form-control" value={this.state.name} />
          </div>
          <div className="form-group">
            <label>Size</label>
            <input onChange={this.onChange} className="form-control" value={this.state.size} />
          </div>
          <div className="form-group">
            <label>Quantity</label>
            <input onChange={this.onChange} className="form-control" value={this.state.quantity} />
          </div>
          <input type="submit" className="btn btn-success" />
        </form>
      </div>
    )
  }
}
