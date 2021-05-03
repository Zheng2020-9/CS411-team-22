import logo from './logo.svg';
import './App.css';
import InfoForm from './InfoForm.js';
import GithubLoginButton from './GithubLoginButton.js';
import MapChart from './MapChart.js';
import ReactDOM from 'react-dom';
import axios from "axios";
import ReactTooltip from "react-tooltip";
import React, { useState, useEffect } from "react";
import BookmarkSidebar from './BookmarkSidebar';


function onClick(e, item) {
  console.log(JSON.stringify(item, null, 2));
}

	const items = [
  { name: 'home', label: 'Home', onClick },
  { name: 'home', label: 'About' },
  {
    name: 'bookmarks',
    label: 'Bookmarks',
    items: [
      { name: 'a', label: 'County A', onClick },
      { name: 'b', label: 'County B', onClick },
    ],
  },
]





function App() {





	const [data, setData] = useState([]);
	



	return (
		<div className='container'>
			<div className='row center'>
				<BookmarkSidebar items={items}/>
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
