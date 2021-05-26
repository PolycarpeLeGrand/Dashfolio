import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import PRES_MD

# Set tab id
TAB_ID = 'home-tab'

home_text_div = html.Div([
    html.H3('Accueil'),
    html.Hr(className='hr-title'),
    html.Br(),
    dcc.Markdown(PRES_MD, className='h5'),
])


home_layout = html.Div([
    home_text_div,
], id=TAB_ID)


