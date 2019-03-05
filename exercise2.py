# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.plotly as py
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/flavors_of_cacao.csv')
# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Exercise 2'),

    # set the description underneath the heading
    html.Div(children='''
        A heat map showing the quality of chocolate by the country of origin and the % cacao.
    '''),



    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                go.Heatmap(x=df['BroadBeanOrigin'],
                           z=df['Rating'],
                           y=df['CocoaPercent'],
                           text=df['SpecificBeanOriginorBarName']
                           )
            ],
            'layout': {
                'title': 'Chocolate Rating by Country and % Cacao',
                'xaxis':{'title':'Cocoa Country of Origin'},
                'yaxis':{'title':'% Cocoa'},
                }
        }
    )

])



if __name__ == '__main__':
    app.run_server(debug=True)

# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.
