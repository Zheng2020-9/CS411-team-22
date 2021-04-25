import logo from './logo.svg';
import './App.css';
import InfoForm from './InfoForm.js';
import ReactDOM from 'react-dom';
import axios from "axios";
import GoogleBtn from './GoogleBtn';



function App() {
	
	



  

  return (
	<div className = 'container'>
    <div className='row center'>
	  <h1>Covid Dashboard App</h1>
		<div className='row center'>
		<InfoForm />

		<GoogleBtn/>

		</div>
    </div>
	</div>
	

  );
}

  ReactDOM.render(<App />, document.getElementById('root'));


export default App;
