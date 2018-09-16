import React from 'react'

export default class Form extends React.Component {
  render() {
    return(
      <form className="resqueue-form">
        <div className="form-group">
          <label>Note</label>
          <input className="form-control" placeholder="Note" />
        </div>
        <div className="form-check">
          <input className="form-check-input" type="checkbox" />
          <label className="form-check-label">Do you require medical assistance?</label>
        </div>
        <div className="form-check">
          <input className="form-check-input" type="checkbox" />
          <label className="form-check-label">Do you require medical assistance?</label>
        </div>
        <div className="form-check">
          <input className="form-check-input" type="checkbox" />
          <label className="form-check-label">Do you require medical assistance?</label>
        </div>
        <input type="submit" value="Please ResQueue Me" className="btn btn-success" />
      </form>
    )
  }
}
