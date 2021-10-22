import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import PRES_MD, APPROCHE_MD

# Set tab id
TAB_ID = 'home-tab'

testimonials = [
    'Très bon cours!',
    'Explications claires, dynamique, on voit que tu es passionné.',
    'À part l\'écriture catastrophique au tableau l\'ensemble était très bien!',
    'Bon dynamisme, A++',
    'Tu vas être un excellent prof, lâche pas même si je déteste la philo!!',
    'Explique très bien la matière, à l\'écoute des élèves, répond bien aux questions et s\'assure que tout le monde a bien compris.',
    'Prenez votre souffle :)',
    'Belle personnalité, belle structure du cours, activités réflectives et intéressantes.',
    'Énergique et intéressant!',
    'Vous êtes très à l\'aise lorsque vient le temps de répondre aux questions ou d\'échanger avec les étudiants.',
    'Bonne présence, pertinent, notes assez claires.',
    'Vous captivez très bien l\'attention des élèves, bonne communication.',
    'Explique bien, répond bien à nos questions, énergique et intéressant.',
    'Très belles explications, apporte de bons exemples concrets pour faciliter la compréhension.',
    'J\'aime bien comment vous vous adressez au groupe et êtes capable de l\'impliquer.',
    'Explique bien la matière, explique en profondeur.',
    'Activité amusante, très intéressant!',
    'Pour un cours que je ne comprends absolument rien, tu as quand même réussi à rendre ça intéressant. Chapeau!',
]

home_text_div = html.Div([
    #html.H3('Accueil'),
    #html.Hr(className='hr-title'),
    #html.Br(),
    dbc.Col([
        dbc.Row([
            dcc.Markdown(PRES_MD, className='md-content'),
        ]),

        dbc.Row([
            html.Div([
                #html.Hr(),
                #html.Div('Quelques témoignages d\'étudiant-e-s:',
                #         style={'color': 'black', 'font-weight': 'bold', 'margin-top': '2rem', 'margin-bottom': '-2rem'}),
                dbc.Carousel(
                    items=[
                        {'key': f'{i}', 'alt': 'Text 1', 'header': t, 'src': 'assets/transparent.svg',
                        'img_style': {'max-height': '6rem'}}
                        for i, t in enumerate(testimonials)
                    ],
                    controls=True,
                    indicators=False,
                    interval=5000,
                    ride='carousel',
                    style={'max-height': '6rem', 'max-width': '75%', 'margin': 'auto'},
                ),
                #html.Hr(),
            ], style={'width': '100%'}),
        ], className='mobile-hidden'),

        dbc.Row([
            dcc.Markdown(APPROCHE_MD, className='md-content'),
        ])
    ]),
])


home_layout = html.Div([
    home_text_div,

], id=TAB_ID)


