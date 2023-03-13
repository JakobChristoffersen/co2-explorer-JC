# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:58:27 2023

@author: Jakob Christoffersen
"""

import pandas as pd
import plotly.express as px
from pandas_datareader import wb

#from jupyter_dash import JupyterDash
from dash import dcc, html, Dash
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css'
load_figure_template('bootstrap')

df_wb = pd.read_csv('world_1960_2021.csv')

  # Rename value column
df_wb.rename(columns = {'EN.ATM.CO2E.KT' : 'CO2 emissions', 'EN.ATM.CO2E.PC' : 'CO2 emissions per capita' }, inplace = True)

df_wb = df_wb.dropna().copy()

df_wb.head()

# Total emissions
fig = px.line(
    df_wb,          # dataframe
    y = 'CO2 emissions',     # column on y-axis
    x = 'year',
     
) 

fig.update_layout(
    yaxis_title = None,                         
    xaxis_title = None,                        
    title = 'Total emissions', 
    title_x = 0.5                              
) 

# Per capita emissions 
fig_2 = px.line(
    df_wb,          # dataframe
    y = 'CO2 emissions per capita',     # column on y-axis
    x = 'year',
     
) 

fig_2.update_layout(
    yaxis_title = None,                         
    xaxis_title = None,                        
    title = 'Per capita emissions', 
    title_x = 0.5                              
) 


app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css])
server = app.server

app.layout = dbc.Container(
    children = [
        
        # Header
        html.H1('CO2 emissions around the world'),
        dcc.Markdown(
            """Data on emissions and potential drivers are extracted from the 
               [World Development Indicators](https://datatopics.worldbank.org/world-development-indicators/) 
               database."""
        ),
        
        dbc.Row(
                    children = [
                        dbc.Col(dcc.Graph(figure = fig),  width = 6),
                        dbc.Col(dcc.Graph(figure = fig_2), width = 6)
                    ]
                )
    
        
    ],
    className = 'dbc'
)

if __name__ == '__main__':
    app.run_server(debug = True)
    
