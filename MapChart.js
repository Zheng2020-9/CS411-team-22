import React, { useState, useEffect } from "react";
import { ZoomableGroup, ComposableMap, Geographies, Geography } from "react-simple-maps";
import { scaleQuantile } from "d3-scale";
import { json } from "d3-fetch";
import { csv } from "d3-fetch";

import axios from "axios";


const geoUrl = "https://cdn.jsdelivr.net/npm/us-atlas@3/counties-10m.json";

const rounded = num => {
	if (num > 1000000000) {
	  return Math.round(num / 100000000) / 10 + "Bn";
	} else if (num > 1000000) {
	  return Math.round(num / 100000) / 10 + "M";
	} else {
	  return Math.round(num / 100) / 10 + "K";
	}
  };

const MapChart = ({ setTooltipContent }) => {
	const [data, setData] = useState([]);
    
    function handleZoomIn() {
        if (position.zoom >= 4) return;
            setPosition(pos => ({ ...pos, zoom: pos.zoom * 2 }));
        }

    function handleZoomOut() {
         if (position.zoom <= 1) return;
            setPosition(pos => ({ ...pos, zoom: pos.zoom / 2 }));
        }

    function handleMoveEnd(position) {
            setPosition(position);
        }
          
	useEffect(() => {
		//CURRENTLY IMPORTING DIRECTLY, UPDATE TO USE DB
		csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv").then(counties => {
			console.log(counties)
			for (var i in counties) {
				counties[i].id = counties[i].fips
				counties[i].name = counties[i].county
				counties[i].state = counties[i].state
				counties[i].case = counties[i].cases
				counties[i].death = counties[i].deaths
				counties[i].c_case = counties[i].confirmed_cases
				counties[i].c_death = counties[i].confirmed_deaths
				counties[i].p_case = counties[i].probable_cases
				counties[i].p_death = counties[i].probable_deaths
				counties[i].date = counties[i].date
			}
			setData(counties);
		});

		const source = axios.CancelToken.source();

		//WE WILL USE THIS LATER WHEN WE IMPORT FROM DB

		//asyn and await allow for standard cleanup (react gets fussy when you do async stuff on components)
		const fetchData = async () => {
			try {
				const response = await axios.get("/api/Counties", {
					cancelToken: source.token
				}).then((res) => {
					var reply = res.data;
					var values = Object.values(reply)

					for (var i in values) {
						values[i].name = values[i].county_name + " County";
						values[i].id = i;
					}
					//console.log(values)
					//setData(values)
				})
			} catch (error) {
				if (axios.isCancel(error)) {

				} else {
					throw error
				}
			}
		};

		fetchData();

		return () => {
			source.cancel();
		};
		//axios.get("/api/Counties/").then((res) => {
		//	var reply = res.data;
		//	var values = Object.values(reply)
		//	var counties = []

		//	for(var i in reply)
		//		counties.push(values[i]);
		//console.log(reply)
		//	console.log(counties)
		//	setData(counties)
		//json(reply).then(counties => {
		//	console.log(counties)
		//	setData(counties);//
		//});

		//}).catch();
	}, []);

	const colorScale = scaleQuantile()
		.domain(data.map(d => d.cases))
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
		<ComposableMap projection="geoAlbersUsa">
            <ZoomableGroup
                      zoom={position.zoom}
                      center={position.coordinates}
                      onMoveEnd={handleMoveEnd}
            >
			<Geographies geography={geoUrl}>
				{({ geographies }) =>
					geographies.map(geo => {
						const cur = data.find(s => s.id === geo.id);
						return (
							<Geography
								key={geo.rsmKey}
								geography={geo}
								fill={cur ? colorScale(cur.cases) : "#EEE"}
								//tooltip hover functions
								onMouseEnter={() => {
									const { NAME, Cov_EST } = geo.properties;
									setTooltipContent(`${NAME} — ${rounded(Cov_EST)}`);
								  }}
								onMouseLeave={() => {
									setTooltipContent("");
								  }}
								  style={{
									hover: {
									  fill: "#0000FF",
									  outline: "none"
									}
								  }}
							/>
						);
					})
				}
			</Geographies>
        </ZoomableGroup>
    </ComposableMap>
    <div className="controls">
    <button onClick={handleZoomIn}>
          <svg
           xmlns="http://www.w3.org/2000/svg"
           width="24"
           height="24"
           viewBox="0 0 24 24"
           stroke="currentColor"
           strokeWidth="3"
          >
            <line x1="12" y1="5" x2="12" y2="19" />
            <line x1="5" y1="12" x2="19" y2="12" />
        </svg>
     </button>
     <button onClick={handleZoomOut}>
          <svg
           xmlns="http://www.w3.org/2000/svg"
           width="24"
           height="24"
           viewBox="0 0 24 24"
           stroke="currentColor"
           strokeWidth="3"
     >
            <line x1="5" y1="12" x2="19" y2="12" />
            </svg>
            </button>
    </div>
	);
};

export default MapChart;
