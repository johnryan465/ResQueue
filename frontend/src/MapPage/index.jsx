import React from 'react'
import Map from './Map'
import Form from './Form'

export default class MapPage extends React.Component {
  render() {
    return(
      <div className="container nopadding">
          <div className="row">
            <div className="col-md-8 nopadding">
              <Map />
            </div>
            <div className="col-md-4">
              <Form />
            </div>
          </div>
      </div>
    );
  }
}
