import React from 'react';
import ReactDOM from 'react-dom';
import axios from "axios";

//InfoForm was the main component for our prototype app.

class InfoForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }
  


  handleSubmit(event) {
	axios.get("/api/States/" +  this.state.value).then((res) => {
		var reply = res.data;
		var report = reply.name + " Covid Report | Cases: " + reply.cases + ", Deaths: " + reply.deaths;  
		alert(report)
	}).catch();
    event.preventDefault();
  }
  


  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default InfoForm;