import React, { Component } from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/route-1" render={() => <h1>Route 1</h1>} />
          <Route path="/route-2" render={() => <h1>Route 2</h1>} />
          <Route path="/route-3" render={() => <h1>Route 3</h1>} />
        </Switch>
      </Router>
    );
  }
}

export default App;
