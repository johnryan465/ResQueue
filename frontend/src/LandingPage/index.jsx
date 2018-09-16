import React from 'react'
import Logo from './Logo'
import { Link } from 'react-router-dom'

export default class LandingPage extends React.Component {
  constructor(props) {
    super(props)
  }
  render() {
    return(
      <div className="container nopadding">
        <div className="row landing-header nopadding">
          <div className="landing-header__content text-center">
              <Logo />
              <Link className="landing-header__button" to="/map">Need Help? Get Resqueued.</Link>
          </div>
        </div>
      </div>
    )
  }
}
