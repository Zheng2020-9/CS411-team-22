import React, { useState, useEffect } from "react";
import { ZoomableGroup, ComposableMap, Geographies, Geography } from "react-simple-maps";
import { scaleQuantile } from "d3-scale";
import { json } from "d3-fetch";
import { csv } from "d3-fetch";

import axios from "axios";


const geoUrl = "https://cdn.jsdelivr.net/npm/us-atlas@3/counties-10m.json";

//React Simple Map's library, from their given example:  https://www.react-simple-maps.io/examples/usa-counties-choropleth-quantize/
//Simple component to display a map of the U.S. with data fetched from the backend server.

const MapChart = ({ setTooltipContent }) => {
	const [data, setData] = useState([]);
	const source = axios.CancelToken.source();

	//Fetch data from public backend API
	const fetchData = async () => {
			try {
				const response = await axios.get("/api/Counties", {
					cancelToken: source.token
				}).then((res) => {
					var reply = res.data;
					var values = Object.values(reply)

					//These fields are required for the mapping library.
					for (var i in values) {
						values[i].name = values[i].county_name;
						values[i].id = values[i].fips;
					}
					console.log(values)
					setData( values);
				})
			} catch (error) {
				if (axios.isCancel(error)) {

				} else {
					throw error
				}
			}
		};

	useEffect(() => {

		fetchData();

		return () => {
			source.cancel();
		};

	}, []);
	
	//Clickhandler for setting bookmarks.
	const handleClick = (geo) => () => {

			const cur = data.find(s => s.id === geo.id);

			var county= cur.name;
			var state= cur.state;
			console.log(county, state);
			localStorage.setItem('county',cur.id);
			localStorage.setItem('county_name',cur.name);



		  };

	//Scale the map colors to fit the data
	const colorScale = scaleQuantile()
		.domain(data.map(d => d.vuln_score))
		.range([
			"#ffedea",
			"#ffcec5",
			"#ffad9f",
			"#ff8a75",
			"#ff5533",
			"#e2492d",
			"#be3d26",
			"#9a311f",
			"#782618"
		]);

	return (
		<ComposableMap data-tip="" projection="geoAlbersUsa">
			<ZoomableGroup>
			<Geographies geography={geoUrl}>
				{({ geographies }) =>
					geographies.map(geo => {
						const cur = data.find(s => s.id === geo.id);
						return (
							<Geography
								key={geo.rsmKey}
								geography={geo}
								fill={cur ? colorScale(cur.vuln_score) : "#EEE"}
								//tooltip hover functions
								onMouseEnter={() => {
									// const [data, setData] = useState([]);
									// const { NAME, POP_EST } = geo.properties;
									//now the map has state and cases info 
									if(cur != null)
									setTooltipContent(`${cur.name}, ${cur.state}  - Vulnerability Score: ${cur.vuln_score} - Weekly Cases: ${(cur.avg_cases)}`);
								  }}
								onMouseLeave={() => {
									setTooltipContent("");
								  }}
								  //css for hover over the map
								  style={{
									hover: {
									  fill: "#36C9C6",
									  outline: "none"
									}
								  }}
								onClick={handleClick(geo)}

							/>
						);
					})
				}
			</Geographies>
			</ZoomableGroup>
		</ComposableMap>
	);
};

export default MapChart;
