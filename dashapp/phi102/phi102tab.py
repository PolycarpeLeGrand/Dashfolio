import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import PLAN102_MD

# Set tab id
TAB_ID = 'phi102-tab'

phi102_content = html.Div([
    dcc.Markdown(PLAN102_MD, className='md-content', style={'text-align': 'justify', 'line-height': '1.5'}),
])

phi102_layout = html.Div([
    phi102_content
], id=TAB_ID)


