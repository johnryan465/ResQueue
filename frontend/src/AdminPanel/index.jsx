import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

export default class AdminPanel extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      vehicles: [{name: "Ford Bus", size: 12, quantity: 3, id: 4}, {name: "Ford Bus", size: 12, quantity: 3, id: 4}, {name: "Ford Bus", size: 12, quantity: 3, id: 4}]
    }
    this.getVehicles = this.getVehicles.bind(this)
  }
  getVehicles() {
    axios.get("/api/vehicles").then((resp) => {
      this.setState({
        vehicles: resp.data
      })
    })
  }
  componentDidMount() {
    //this.getVehicles()
  }
  render() {
    const vehicleRows = this.state.vehicles.map((vehicle) =>
      <tr>
        <td>{vehicle.name}</td>
        <td>{vehicle.size}</td>
        <td>{vehicle.quantity}</td>
        <td>
          <Link to={`/admin/vehicles/${vehicle.id}`}>Edit</Link>
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
          </tbody>
        </table>
      </div>
    );
  }
}
