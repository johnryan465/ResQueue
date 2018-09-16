import React from 'react'
import axios from 'axios'

export default class Form extends React.Component {
  render() {
    return(
      <form className="resqueue-form">
        <span className="btn btn-success" onClick={this.props.onClick}>Calculate Route</span>
      </form>
    )
  }
}
