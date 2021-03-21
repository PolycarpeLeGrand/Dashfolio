import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from tools.factories import jumbotron_2_columns
from dashapp import app, MAT_MD, SEQ_MD, AUTH_MD, CONSPI_MD, GRILLE_MD, QUESTIONNAIRE_MD

# Set tab id
TAB_ID = 'material-tab'

material_pres_card = dbc.Card([
    html.H3('Présentation des cours'),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),
    dcc.Markdown('En construction, mise à jour imminente!', className='h6'),
    #html.Iframe(src='https://giphy.com/embed/6uGhT1O4sxpi8', style={'margin': '5px', 'border': 'none'}),

    html.H3('Exemples de matériel', style={'padding-top': '20px'}),
    html.Hr(style={'width': '30%', 'text-align': 'left', 'margin-left': '0px'}),
    html.Br(),

    dcc.Markdown(MAT_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),
    html.Br(), html.Br(),

    dcc.Markdown(SEQ_MD, className='h5', style={'margin-bottom': 0, 'text-align': 'justify', 'line-height': '1.5'}),
    html.A('Séquence d\'évaluation', href='assets/sequence.pdf', target='_blank', style={'text-decoration': 'underline'}, className='h5'),
    html.Br(), html.Br(),

    dcc.Markdown(AUTH_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),
    dbc.Container([
        html.Iframe(src='https://www.youtube.com/embed/31Sgq_O4COo',
                    style={'position': 'absolute', 'top': '0', 'bottom': '0', 'border': 'none', 'width': '100%','height': '100%'}),
    ], style={'position': 'relative', 'width': '90%', 'height': '0', 'padding-left': '0', 'padding-bottom': '56.25%', 'margin-bottom': '30px'}),
    html.Br(), html.Br(),

    dcc.Markdown(GRILLE_MD, className='h5', style={'margin-bottom': 0, 'text-align': 'justify', 'line-height': '1.5'}),
    html.A('Grille d\'évaluation', href='assets/grille.pdf', target='_blank', style={'text-decoration': 'underline'}, className='h5'),
    html.Br(), html.Br(),

    dcc.Markdown(QUESTIONNAIRE_MD, className='h5', style={'margin-bottom': 0, 'text-align': 'justify', 'line-height': '1.5'}),
    html.A('Questionnaire « Pour mieux vous connaitre »', href='https://docs.google.com/forms/d/e/1FAIpQLSdYA4-9au6Jrn76PrPcG5s3ZX5LXFqjPi48pz5dSsbmA_-GaQ/viewform?usp=sf_link', target='_blank', style={'text-decoration': 'underline'}, className='h5'),
    html.Br(), html.Br(),

    dcc.Markdown(CONSPI_MD, className='h5', style={'text-align': 'justify', 'line-height': '1.5'}),
    dbc.Container([
        html.Iframe(src='https://www.youtube.com/embed/kYEUH0NBO7I',
                    style={'position': 'absolute', 'top': '0', 'bottom': '0', 'border': 'none', 'width': '100%', 'height': '100%'}),
    ], style={'position': 'relative', 'width': '90%', 'height': '0', 'padding-left': '0', 'padding-bottom': '56.25%', 'margin-bottom': '30px'}),
    html.Br(), html.Br(),

], body=True)


material_tab_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            material_pres_card,
        ], xs=12, lg=6)
    ], justify='center'),

], fluid=True, id=TAB_ID)

