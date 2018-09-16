import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

export default class AdminPanel extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      vehicles: []
    }
    this.getVehicles = this.getVehicles.bind(this)
    this.addVehicle = this.addVehicle.bind(this)
  }
  getVehicles() {
    axios.get("/api/vehicles").then((resp) => {
      this.setState({
        vehicles: resp.data
      })
    })
  }
  addVehicle() {
    axios.post("/api/vehicles", {
      name: "",
      quantity: 1,
      size: 5
    }).then(({data:id}) => {
      window.location = `/admin/vehicles/${id}`
    })
  }
  componentDidMount() {
    this.getVehicles()
  }
  render() {
    const vehicleRows = this.state.vehicles.map((vehicle) =>
      <tr>
        <td>{vehicle.name}</td>
        <td>{vehicle.size}</td>
        <td>{vehicle.quantity}</td>
        <td>
          <Link to={`/admin/vehicles/${vehicle._id}`}>Edit</Link>
        </td>
      </tr>
    )
    return(
      <div className="admin-panel">
        <table className="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Size</th>
              <th>Quantity</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            { vehicleRows }
            <tr>
              <td></td>
              <td></td>
              <td></td>
              <td>
                <span onClick={this.addVehicle} className="btn btn-success">Add New Vehicle</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
}
