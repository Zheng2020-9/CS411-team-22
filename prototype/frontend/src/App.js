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

//Default subitems array for sidebar, when receiving 404 from backend.
var subItems = [
      { name: 'a', label: 'County A', onClick },
      { name: 'b', label: 'County B', onClick },
    ];


//Clickhandler for sidebar buttons
async function onClick(e, item) {
	const source = axios.CancelToken.source();

  console.log(JSON.stringify(item, null, 2));
  try{
  const response = await axios.get("/api/Counties/" + item.name, {
					cancelToken: source.token
				}).then((res) => {
					var reply = res.data;
					var report = reply.county_name + " Covid Report | Weekly Cases: " + reply.avg_cases + ",Weekly Deaths: " + reply.avg_deaths;  
					alert(report)
				})
  } catch(err){
	  
  }
}

//API request to add a bookmark
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


//County names are fetched from backend
const updateNames = async (arr) =>{
	var county_names = [];
			const source = axios.CancelToken.source();

	for(const index in arr){
				const response = await axios.get("/api/Counties/" + arr[index], {
					cancelToken: source.token
				}).then((res) => {
					var reply = res.data;
					console.log("LABEL REPLY: " + reply.data);
					var report = reply.county_name + " Covid Report | Weekly Cases: " + reply.avg_cases + ",Weekly Deaths: " + reply.avg_deaths;  
					county_names.push(reply.county_name);
				})
			}
	return county_names;
}
	
//Bookmarks are fetched from backend
const updateBookmarks = async () =>{
	console.log("Updating bookmarks");
		const source = axios.CancelToken.source();

	const params = {token: localStorage.getItem('token'), command: "getBM"};
		console.log(JSON.stringify(params));

	try{
			let response = await axios.post('/useroperate/',params);
			console.log(response.data);
			console.log(response.data.BM);
			var bookmarks = response.data.BM;
			var arr = bookmarks.split(",");
			
			var items1 = [];
			
			var county_names = await updateNames(arr);
			
			for(const index in arr){
				items1.push( { name: arr[index], label: county_names[index], onClick})
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
	}catch(err){}
}


	return (
		<div className='container'>
			<div className='row center'>
				<BookmarkSidebar items={items}/>
				<h1>Covid Dashboard App</h1>
				<div className='row center'>
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
