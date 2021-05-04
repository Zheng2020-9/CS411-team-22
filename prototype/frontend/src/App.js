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

function addBookmark() {
	var county = localStorage.getItem('county');
    var county_name = localStorage.getItem('county_name');
	if(county != null){
		alert("Added " + county_name + " to bookmarks");
		const params = {token: localStorage.getItem('token'), command: "addBM", BM: county};
		console.log(JSON.stringify(params));
		try{
			 axios.post('/useroperate/', params);
		}catch(err){

		}
	}

}





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
					
					
					 <button onClick={() => addBookmark()}>
					 Bookmark Selected County
     				 </button>

					
					
				</div>
			</div>
		</div>


	);
}

ReactDOM.render(<App />, document.getElementById('root'));


export default App;
