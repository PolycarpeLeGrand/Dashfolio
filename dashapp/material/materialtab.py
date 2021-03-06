import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import MAT_MD, SEQ_MD, AUTH_MD, CONSPI_MD, GRILLE_MD, QUESTIONNAIRE_MD

# Set tab id
TAB_ID = 'material-tab'

material_content_micro = html.Div([
    html.H3('Exemples de matériel'),
    html.Hr(className='hr-title'),
    html.Br(),

    dcc.Markdown(MAT_MD, className='h5'),
    html.Br(), html.Br(),

    dcc.Markdown(SEQ_MD, className='h5', style={'margin-bottom': 0}),
    html.A('Séquence d\'évaluation', href='assets/sequence.pdf', target='_blank', style={'text-decoration': 'underline'}, className='h5'),
    html.Br(), html.Br(),

    dcc.Markdown(AUTH_MD, className='h5'),
    dbc.Container([
        html.Iframe(src='https://www.youtube.com/embed/31Sgq_O4COo',
                    style={'position': 'absolute', 'top': '0', 'bottom': '0', 'border': 'none', 'width': '100%','height': '100%'}),
    ], style={'position': 'relative', 'width': '90%', 'height': '0', 'padding-left': '0', 'padding-bottom': '56.25%', 'margin-bottom': '30px'}),
    html.Br(), html.Br(),

    dcc.Markdown(GRILLE_MD, className='h5', style={'margin-bottom': 0}),
    html.A('Grille d\'évaluation', href='assets/grille.pdf', target='_blank', style={'text-decoration': 'underline'}, className='h5'),
    html.Br(), html.Br(),

    dcc.Markdown(QUESTIONNAIRE_MD, className='h5', style={'margin-bottom': 0}),
    html.A('Questionnaire « Pour mieux vous connaitre »', href='https://docs.google.com/forms/d/e/1FAIpQLSdYA4-9au6Jrn76PrPcG5s3ZX5LXFqjPi48pz5dSsbmA_-GaQ/viewform?usp=sf_link', target='_blank', style={'text-decoration': 'underline'}, className='h5'),
    html.Br(), html.Br(),

    dcc.Markdown(CONSPI_MD, className='h5'),
    dbc.Container([
        html.Iframe(src='https://www.youtube.com/embed/kYEUH0NBO7I',
                    style={'position': 'absolute', 'top': '0', 'bottom': '0', 'border': 'none', 'width': '100%', 'height': '100%'}),
    ], style={'position': 'relative', 'width': '90%', 'height': '0', 'padding-left': '0', 'padding-bottom': '56.25%', 'margin-bottom': '30px'}),
    html.Br(), html.Br(),

])

material_head = html.Div([
    html.H3('Exemples de matériel'),
    html.Hr(className='hr-title'),
    html.Br(),

    dcc.Markdown('Materiel et cie'),
    html.Br(),

    dbc.Tabs([
        dbc.Tab(material_content_micro, label='Microprogramme'),
        dbc.Tab(material_content_micro, label='Documents'),
        dbc.Tab(material_content_micro, label='Ateliers et Activités'),

    ])

])

material_layout = html.Div([
    # material_head,
    # html.Div(id='material-content-div')
    material_content_micro,
], id=TAB_ID)

