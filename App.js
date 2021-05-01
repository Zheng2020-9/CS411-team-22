import React, { Component } from "react";

const todoItems = [
  {
    id: 1,
    name: "test",
    state_name: "2021-03-26 21:13:03.798745+00:00",
    stats: 100,
  },
  {
    id: 2,
    name: "test2",
    state_name: "2021-03-26 21:13:03.798745+00:00",
    stats: 100,
  },
  {
    id: 3,
    name: "test3",
    state_name: "2021-03-26 21:13:03.798745+00:00",
    stats: 100,
  },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: 100,
      todoList: todoItems,
    };
  }

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: 3});
    }

    return this.setState({ viewCompleted: 4});
  };

  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span
          className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
          onClick={() => this.displayCompleted()}

        >
          statistics
        </span>
      </div>
    );
  };


  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList.filter(
      (item) => item.stats == viewCompleted
    );

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.state_name}
        >
          {item.stats}
        </span>
        <span>
          <button
            className="btn btn-secondarfy mr-2"
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                >
                  Add task
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;