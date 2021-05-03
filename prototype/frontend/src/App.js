import logo from './logo.svg';
import './App.css';
import InfoForm from './InfoForm.js';
import GithubLoginButton from './GithubLoginButton.js';
import MapChart from './MapChart.js';
import ReactDOM from 'react-dom';
import axios from "axios";
import ReactTooltip from "react-tooltip";
import React, { useState, useEffect } from "react";


function App() {






	const [data, setData] = useState([]);

	return (
		<div className='container'>
			<div className='row center'>
				<h1>Covid Dashboard App</h1>
				<div className='row center'>
					<InfoForm />
					<script>

					</script>
					<GithubLoginButton />
					
					<MapChart setTooltipContent={setData} />
     				<ReactTooltip>{data}</ReactTooltip>
				</div>
			</div>
		</div>


	);
}

ReactDOM.render(<App />, document.getElementById('root'));


export default App;
