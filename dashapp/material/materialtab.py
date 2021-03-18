import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from tools.factories import jumbotron_2_columns
from dashapp import app

# Set tab id
TAB_ID = 'material-tab'

material_pres_card = dbc.Card([
    html.H3('Présentation des cours'),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),
    dcc.Markdown('En construction, mise à jour imminente!', className='h6'),
    html.Iframe(src='https://giphy.com/embed/6uGhT1O4sxpi8', style={'margin': '5px', 'border': 'none'}),
    html.H3('Exemples de matériel'),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),
    html.Iframe(src='https://www.youtube.com/embed/31Sgq_O4COo', style={'margin': '5px', 'height': '100%', 'width': '100%','border': 'none'}),
    html.Iframe(src='https://www.youtube.com/embed/kYEUH0NBO7I', style={'margin': '5px', 'border': 'none'})
], body=True)


material_tab_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            material_pres_card,
        ], xs=12, lg=6)
    ], justify='center'),

], fluid=True, id=TAB_ID)

