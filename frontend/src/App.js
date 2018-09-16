import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import MapPage from './MapPage'
import AdminPanel from './AdminPanel'
import EditVehiclePage from './EditVehiclePage'
import AdminMap from './AdminMap'
import LandingPage from './LandingPage'

import 'bootstrap/dist/css/bootstrap.css'
import './App.css'

class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/" exact component={ LandingPage } />
          <Route path="/map" component={ MapPage } />
          <Route path="/admin/vehicles" exact component={ AdminPanel } />
          <Route path="/admin/vehicles/:id" component={ EditVehiclePage } />
          <Route path="/admin/map" component={ AdminMap } />
          <Route path="/*" render={() => <h1>404</h1>} />
        </Switch>
      </Router>
    );
  }
}

export default App;
