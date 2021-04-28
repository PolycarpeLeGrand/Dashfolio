import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import PLAN101_MD

# Set tab id
TAB_ID = 'phi101-tab'

phi101_content_card = dbc.Card([
    html.H3('Philosophie et rationalité'),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),
    dcc.Markdown(PLAN101_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),
], body=True)


phi101_tab_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            phi101_content_card,
        ], xs=12, lg=6)
    ], justify='center'),

], fluid=True, id=TAB_ID)

