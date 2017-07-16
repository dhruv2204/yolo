import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Sheet from './Sheet';
import "ag-grid/dist/styles/ag-grid.css";
import "ag-grid/dist/styles/theme-fresh.css";

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Python API example with ag-grid</h2>
          <h4>Spreadsheet</h4>
        </div>
        <p className="App-intro">
          Below is the sheet with data <code>testdb</code> and fetched from python API.
        </p>
        <Sheet/>
      </div>
    );
  }
}

export default App;
