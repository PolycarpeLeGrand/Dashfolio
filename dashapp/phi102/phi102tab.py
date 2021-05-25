import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import PLAN102_MD

# Set tab id
TAB_ID = 'phi102-tab'


phi102_content = html.Div([
    html.H3('L\'être humain'),
    html.Hr(className='hr-title'),
    html.Br(),
    dcc.Markdown('Placeholder', className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),

    #html.H3('Exemples de matériel', style={'padding-top': '20px'}),
    html.Hr(className='hr-title'),
    html.Br(),
    dcc.Markdown(PLAN102_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),
])


phi102_layout = html.Div([
    phi102_content
], id=TAB_ID)


