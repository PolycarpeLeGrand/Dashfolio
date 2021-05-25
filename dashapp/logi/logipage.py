import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ALL, MATCH
import json
from dashapp.logi.logic import *
import random
from dash import callback_context

from dashapp import app, LOGI_MD, LOGI_INST_MD
from dashapp.logi.logitext import PREM_TEMPLATES

PROPS = ['P', 'Q', 'R', 'S', 'T']
PROPS_WITH_NEG = PROPS + [f'non-{p}' for p in PROPS]

SENTS = {
    'P': 'Le ciel est bleu',
    'Q': 'La mer est calme',
    'R': 'Les oiseaux gazouillent',
    'S': 'La baleine chante',
    'T': 'Le marin prie',
}

# Set tab id
TAB_ID = 'logi-tab'

logi_title_div = html.Div([
    html.H3('Logique et argumentation'),
    html.Hr(className='hr-title'),
    html.Br(),
    dcc.Markdown(LOGI_MD, className='h5'),
    html.Button('Mode d\'emploi', id='logi-modal-btn', className='logi-btn', style={'margin-bottom': '24px'}),
    dbc.Modal([
        dbc.ModalBody([dcc.Markdown(LOGI_INST_MD, className='h5')]),
    ], centered=True, id='logi-modal'),
])


logi_add_text_prem_div = html.Div([
    dbc.InputGroup([dbc.InputGroupAddon(f'Prémisse:', addon_type="prepend"),
                    dbc.Input(id=f'logi-prem-text-input', type='text',
                              placeholder='Entrer la proposition sous forme textuelle'),
                    dbc.InputGroupAddon(
                        html.Button('Ajouter', id="logi-prem-text-button", className='logi-btn'), addon_type="append"),
                    ],
                   style={'margin-bottom': '3px'}),
    dbc.Form([
        dbc.FormGroup([
            dbc.InputGroup([
                dbc.InputGroupAddon('Type de proposition:', addon_type="prepend"),
                dbc.Select(id='logi-prem-type-0',
                           options=[
                               {'label': 'Proposition atomique', 'value': 'simple'},
                               {'label': 'Implication', 'value': 'if'},
                               {'label': 'Conjonction', 'value': 'and'},
                               {'label': 'Disjonction', 'value': 'or'},
                           ],
                           value='simple'),
            ], style={'max-width': '25rem'}),
        ]),
        dbc.FormGroup([
            dbc.InputGroup([
                dbc.InputGroupAddon('Entre:', addon_type='prepend'),
                dbc.Select(id='logi-prem-type-1',
                           options=[
                               {'label': 'Proposition atomique', 'value': 'simple'},
                               {'label': 'Implication', 'value': 'if'},
                               {'label': 'Conjonction', 'value': 'and'},
                               {'label': 'Disjonction', 'value': 'or'},
                           ],
                           value='simple'),
            ], style={'max-width': '25rem'}),
        ]),
        dbc.FormGroup([
            dbc.InputGroup([
                dbc.InputGroupAddon('Et:', addon_type='prepend'),
                dbc.Select(id='logi-prem-type-2',
                           options=[
                               {'label': 'Proposition atomique', 'value': 'simple'},
                               {'label': 'Implication', 'value': 'if'},
                               {'label': 'Conjonction', 'value': 'and'},
                               {'label': 'Disjonction', 'value': 'or'},
                           ],
                           value='simple'),
            ]),
        ]),
    ], inline=True),
], style={'padding': '0.5rem', 'border': '1px solid black'})


logi_arg_prems_div = html.Div([

], id='logi-arg-prems-div', style={'min-height': '40px'})


logi_arg_conc_div = html.Div([
    dbc.Label('C - ', className='h5', style={'padding-right': '6px'}),
    dbc.Select(id='logi-conc-select', style={'max-width': '100px'},
               options=[
                   {'label': p, 'value': p} for p in PROPS_WITH_NEG
               ]),
    html.Button('Évaluer!', id='logi-eval-btn', className='logi-btn', style={'margin-left': '30px'}),
])

logi_arg_div = html.Div([
    html.Div(json.dumps({'premises': []}), id='logi-arg-json-div', style={'display': 'none'}),
    logi_arg_prems_div,
    html.Hr(style={'width': '40%', 'text-align': 'left', 'margin-left': '0px'}),
    logi_arg_conc_div,
    html.H5(id='logi-result', style={'margin-top': '24px'}),
    html.H5(id='logi-result-text', style={'margin-top': '24px'}),
], style={'padding-top': '50px',})

logi_paragraph_div = html.Div([

])

logi_layout = html.Div([
    dbc.Row([
        dbc.Col([
            logi_title_div,
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            logi_add_text_prem_div,
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            logi_arg_div,
        ], style={'max-width': '720px'}),
        # dbc.Col([

        # ], xs=0, lg=2),
    ], justify='start'),
], id=TAB_ID)


def fn(p):
    """format negative, take a premise (P or non-P), returns (P or ~P)"""

    return p.replace('non-', '~')


def prem_to_text(prem, mapping):
    if ' >> ' in prem:
        op = ' >> '
    elif ' & ' in prem:
        op = ' & '
    elif ' | ' in prem:
        op = ' | '
    elif ' |= ' in prem:
        op = ' |= '
    else:
        op = 'simple'

    p1 = prem if op == 'simple' else prem.split(op)[0]
    p2 = '' if (op == 'simple' or op == ' |= ') else prem.split(op)[1]

    p1 = p1.replace('~', random.choice(PREM_TEMPLATES['neg']) + ' ').replace(p1[-1], mapping[p1[-1]])
    if p2 != '':
        p2 = p2.replace('~', random.choice(PREM_TEMPLATES['neg']) + ' ').replace(p2[-1], mapping[p2[-1]])

    s = random.choice(PREM_TEMPLATES[op]).replace('*1*', p1).replace('*2*', p2)

    return s


def arg_to_text(prems, conc, mapping):
    # Remove upper case and period in prem texts
    for v, s in mapping.items():
        mapping[v] = s[:1].lower() + s[1:].replace('.', '') if s else v

    prem_strings = []
    for prem in prems:
        prem_strings.append(prem_to_text(prem, mapping))

    conc = prem_to_text(conc + ' |= ', mapping)

    text = ' '.join(prem.capitalize() for prem in prem_strings) + ' ' + conc.capitalize()

    return text


def make_new_prem(text, type_0, type_1, type_2):



    return dbc.FormGroup([
        dbc.Label(text),
        dbc.Select(
            options=[
                {'label': p, 'value': p} for p in PROPS_WITH_NEG
            ],
            style={'max-width': '20px'},
        ),

    ], row=True)


@app.callback(
    [Output('logi-arg-prems-div', 'children'),
     Output('logi-prem-text-input', 'value')],
    [Input('logi-prem-text-input', 'n_submit'),
     Input('logi-prem-text-button', 'n_clicks')],
    [State('logi-arg-prems-div', 'children'),
     State('logi-prem-text-input', 'value'),
     State('logi-prem-type-0', 'value'),
     State('logi-prem-type-1', 'value'),
     State('logi-prem-type-2', 'value'),
     ], prevent_initial_call=True
)
def logi_update(new_prem_text_submit, new_prem_text_btn, prems_div, new_prem_text,
                prem_type_0, prem_type_1, prem_type_2):
    print(prems_div)
    trigger_id = callback_context.triggered[0]['prop_id'].split('.')[0]
    if trigger_id in ('logi-prem-text-input', 'logi-prem-text-button'):
        prems_div.append(make_new_prem(new_prem_text, prem_type_0, prem_type_1, prem_type_2))
        new_prem_text = ''
        html.Div()
    return prems_div, new_prem_text


@app.callback(
    Output('logi-modal', 'is_open'),
    [Input('logi-modal-btn', 'n_clicks')],
    [State('logi-modal', 'is_open')],
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open
