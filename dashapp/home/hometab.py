import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from tools.factories import jumbotron_2_columns
from dashapp import app, PRES_MD

# Set tab id
TAB_ID = 'home-tab'

home_text_card = dbc.Card([
    html.H3('Présentation générale'),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),
    dcc.Markdown(PRES_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),
], body=True)

home_tab_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            home_text_card,
        ], xs=12, lg=6)
    ], justify='center'),

], fluid=True, id=TAB_ID)

