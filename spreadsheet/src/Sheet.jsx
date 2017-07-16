import React, {Component} from "react";
import {AgGridReact} from "ag-grid-react";

export default class extends Component {
    constructor(props) {
        super(props);

        this.state = {
            columnDefs: this.createColumnDefs(),
            rowData: this.createRowData()
        }
    }

    onGridReady(params) {
        this.gridApi = params.api;
        this.columnApi = params.columnApi;

        this.gridApi.sizeColumnsToFit();
    }

    createColumnDefs() {
        return [
            {headerName: "Name", field: "name"},
            {headerName: "Employee_Id", field: "e_id"},
            {headerName: "Value", field: "value_in_company"}
        ];
    }

    createRowData() {
        return [{"e_id":3,"m_id":1,"name":"Pappan","value_in_company":27},
                {"e_id":10,"m_id":3,"name":"Gandhi","value_in_company":15},
                {"e_id":11,"m_id":3,"name":"Elon","value_in_company":15},
                {"e_id":12,"m_id":3,"name":"Musk","value_in_company":13},
                {"e_id":13,"m_id":3,"name":"Dan","value_in_company":14}
                ];
    }

    render() {
        let containerStyle = {
            height: 115,
            width: 500
        };

        return (
            <div style={containerStyle} className="ag-fresh">
                <h1>Simple ag-Grid React Example</h1>
                <AgGridReact
                    // properties
                    columnDefs={this.state.columnDefs}
                    rowData={this.state.rowData}

                    // events
                    onGridReady={this.onGridReady}>
                </AgGridReact>
            </div>
        )
    }
};
