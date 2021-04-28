import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import PLAN102_MD

# Set tab id
TAB_ID = 'phi102-tab'


phi102_content_card = dbc.Card([
    html.H3('L\'être humain'),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),
    dcc.Markdown('Placeholder', className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),

    #html.H3('Exemples de matériel', style={'padding-top': '20px'}),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),
    dcc.Markdown(PLAN102_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),

], body=True)


phi102_tab_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            phi102_content_card,
        ], xs=12, lg=6)
    ], justify='center'),

], fluid=True, id=TAB_ID)

