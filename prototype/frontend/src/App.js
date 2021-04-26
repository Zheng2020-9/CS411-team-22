import logo from './logo.svg';
import './App.css';
import InfoForm from './InfoForm.js';
import React from 'react';
import ReactDOM from 'react-dom';
import axios from "axios";




class App extends React.Component {

  insertGapiScript() {
    const script = document.createElement('script')
    script.src = 'https://apis.google.com/js/api.js'
    script.onload = () => {
      this.initializeGoogleSignIn()
    }
    document.body.appendChild(script)
  }

  initializeGoogleSignIn() {
    window.gapi.load('auth2', () => {
      window.gapi.auth2.init({
        client_id: '277403998690-n37ruvh63adulkb70tr21of851iducdc.apps.googleusercontent.com'
      })
      console.log('Api inited')

      window.gapi.load('signin2', () => {
        const params = {
          onsuccess: () => {
            console.log('User has finished signing in!')
          }
        }
        window.gapi.signin2.render('loginButton', params)
      })
    })
  }

  componentDidMount() {
    console.log('Loading')

    this.insertGapiScript();
  }

  render() {
    return (
      <div className="App">
        <h1>Covid Dashboard</h1>
        <a id="loginButton">Sign in with Google</a>
        		<div className='row center'>
		<InfoForm />
		</div>
      </div>
    );
  }
}

export default App;
