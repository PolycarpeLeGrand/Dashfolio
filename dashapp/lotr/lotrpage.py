import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash

from dashapp import app, LOTR_MD
from dashapp.lotr.lotrdata import LOTR_DATA

# Set tab id
PAGE_ID = 'lotr-page'

lotr_intro_div = html.Div([
    dcc.Markdown(LOTR_MD, className='md-content'),
])

lotr_game_div = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H4('', id='lotr-question-title'),
            dcc.Store(id='lotr-game-state', data={'score': 0, 'allow_answers': '', 'current_question': 0})
        ], width=10)
    ]),
    dbc.Row([
        dbc.Col([
            html.H1('', id='lotr-name-title'),
        ], width=10, align='center'),
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            html.Button('Philosophe', className='lotr-answer-btn', id='lotr-philo-btn'),
        ], width=6, style={'text-align': 'right'}),
        dbc.Col([
            html.Button('Seigneur des Anneaux', className='lotr-answer-btn', id='lotr-lotr-btn'),
        ], width=6),
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            html.H3('', id='lotr-result-title'),
        ], width=10)
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('', id='lotr-result-details', style={'text-align': 'left'}),
        ], width=12)
    ], justify='center'),
    dbc.Row([
        dbc.Col([
            html.Button('Question Suivante', id='lotr-next-btn'),
        ], width=10, style={'text-align': 'center'})
    ], justify='center')
], style={'margin-top': '4rem', 'margin-left': '0', 'max-width': '30rem'})


lotr_layout = html.Div([
    lotr_intro_div,
    lotr_game_div,
], id=PAGE_ID)


def show_new_question():
    return


def show_answer():
    return


@app.callback(
    [Output('lotr-name-title', 'children'),
     Output('lotr-result-title', 'children'),
     Output('lotr-result-details', 'children'),
     Output('lotr-next-btn', 'style'),
     Output('lotr-philo-btn', 'disabled'),
     Output('lotr-lotr-btn', 'disabled',),
     Output('lotr-game-state', 'data'),
     Output('lotr-philo-btn', 'style'),
     Output('lotr-lotr-btn', 'style'),],
    [Input('lotr-philo-btn', 'n_clicks'),
     Input('lotr-lotr-btn', 'n_clicks'),
     Input('lotr-next-btn', 'n_clicks'),],
    [State('lotr-game-state', 'data')]
)
def update_game_content(philo_clicks, lotr_clicks, next_clicks, game_state):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id in ['lotr-philo-btn', 'lotr-lotr-btn']:
        question_number = game_state['current_question']
        data = LOTR_DATA[question_number - 1]

        correct = button_id.split('-')[1] == data['answer']
        if correct:
            game_state['score'] += 1

        result_title = 'Bonne réponse!' if correct else 'Oups!'
        result_details = data['details']
        game_state['allow_answers'] = True

    else:
        game_state['current_question'] += 1
        question_number = game_state['current_question']

        result_title = ''
        result_details = ''
        game_state['allow_answers'] = False

    if question_number <= len(LOTR_DATA):
        return f'{LOTR_DATA[question_number - 1]["name"]}', \
            result_title, \
            result_details, \
            {'visibility': 'hidden'} if not game_state['allow_answers'] else {}, \
            game_state['allow_answers'], \
            game_state['allow_answers'], \
            game_state, \
            {}, \
            {},

    else:
        return 'Terminé!', \
            f'Note finale: {game_state["score"]}/{len(LOTR_DATA)}', \
            '', \
            {'visibility': 'hidden'}, \
            True, \
            True, \
            game_state, \
            {'visibility': 'hidden', 'height': '0'}, \
            {'visibility': 'hidden', 'height': '0'}

