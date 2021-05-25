import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import PLAN101_MD

# Set tab id
TAB_ID = 'phi101-tab'

phi101_content = html.Div([
    html.H3('Philosophie et rationalité'),
    html.Hr(className='hr-title'),
    html.Br(),
    dcc.Markdown(PLAN101_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),
])

phi101_layout = html.Div([
    phi101_content
], id=TAB_ID)


