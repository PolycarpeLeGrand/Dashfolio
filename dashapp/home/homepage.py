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
    dcc.Markdown('Bonjour! Le site est en train d\'être mis à jour, ce texte changera sous peu.'),
    #dcc.Markdown(PRES_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),

    html.H3('Mon approche'),
    html.Hr(className='hr-title'),
    html.Br(),
    dcc.Markdown(PRES_MD, className='h5'),
])


home_layout = html.Div([
    home_text_div,
], id=TAB_ID)


