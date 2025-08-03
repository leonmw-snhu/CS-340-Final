from dash import html, dcc, dash_table, Input, Output
import dash_bootstrap_components as dbc
from animal_dashboard.models.animal_shelter import AnimalShelter
from dash_ag_grid import AgGrid

import pandas as pd

# Convert to DataFrame


def serve_layout():
    shelter = AnimalShelter(
        username='aacuser', password='password')  # Create instance
    try:
        data = shelter.read_all()
    except Exception as e:
        data = []
        print(f"Error reading from shelter DB: {e}")
    df = pd.DataFrame(data)
    return dbc.Container([
        html.H1("Animal Shelter Dashboard", className="mb-4"),
        html.Div([
            html.H5(f"Total Records: {len(data)}"),
            html.P(f"Unique Breeds: {df['breed'].nunique()}"),
            html.P(
                f"Date Range: {df['date_of_birth'].min()} to {df['date_of_birth'].max()}"),
        ]),
        AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"headerName": col, "field": col, "filter": True}
                        for col in df.columns],
            defaultColDef={
                "sortable": True,
                "filter": True,
                "floatingFilter": True,
                "resizable": True,
            },
            style={"height": "600px", "width": "100%"},
        )
    ])
