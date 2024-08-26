# src/dashboard.py
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

def create_dashboard(data):
    app = dash.Dash(__name__)

    fig = px.line(data, x='date', y='value', title='Time Series Forecast')

    app.layout = html.Div(children=[
        html.H1(children='Predictive Analytics Dashboard'),
        dcc.Graph(id='example-graph', figure=fig)
    ])

    app.run_server(debug=True)


