import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash
import random

from dashapp import app


dice_layout = html.Div([

    html.H2('Cliquez sur le bouton pour rouler le dé.', style={'text-align': 'center'}),
    html.Div(dbc.Button('Rouler!', id='dice-button', color='primary', style={'padding': '0.5rem 1rem', 'font-size': '1.3rem'}), style={'text-align': 'center', 'margin': '2rem'}),
    html.H3('', id='dice-result', style={'text-align': 'center'}),
], style={})


@app.callback(
    Output('dice-result', 'children'),
    [Input('dice-button', 'n_clicks'),], prevent_initial_call=True
)
def roll_dice(click, sides=20):
    return f'Résultat: {random.randint(1,20)}'

