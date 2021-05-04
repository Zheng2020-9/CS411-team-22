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

var subItems = [
      { name: 'a', label: 'County A', onClick },
      { name: 'b', label: 'County B', onClick },
    ];


function onClick(e, item) {
  console.log(JSON.stringify(item, null, 2));
}

//var items = [
 // { name: 'home', label: 'Home', onClick },
 // { name: 'home', label: 'About' },
 // {
 //   name: 'bookmarks',
 //   label: 'Bookmarks',
 //   subItems,
 // },
//]

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
	const [items, setItems] = useState([
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
]);




	
const updateBookmarks = async () =>{
	console.log("Updating bookmarks");
	const params = {token: localStorage.getItem('token'), command: "getBM"};
		console.log(JSON.stringify(params));

	try{
			let response = await axios.post('/useroperate/',params);
			console.log(response.data);
			console.log(response.data.BM);
			var bookmarks = response.data.BM;
			var arr = bookmarks.split(",");
			
			var items1 = [];
			for(const index in arr){
				items1.push( { name: arr[index], label: arr[index]})
			}
			console.log("Bookmarks: ");
			console.log(items1);
				setItems( [
  { name: 'home', label: 'Home', onClick },
  { name: 'home', label: 'About' },
  {
    name: 'bookmarks',
    label: 'Bookmarks',
    items: items1,
  },
]);


	}catch(err){
	
	}
}


	return (
		<div className='container'>
			<div className='row center'>
				<BookmarkSidebar items={items}/>
				<h1>Covid Dashboard App</h1>
				<div className='row center'>
					<InfoForm />
					<script>

					</script>
					<GithubLoginButton bookmarkUpdater={updateBookmarks} />
					
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
