import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
from dashapp.logi.logic import *
import random

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

logi_propositions_div = html.Div(
    [
        dbc.InputGroup([dbc.InputGroupAddon(f'Proposition {p}', addon_type="prepend"),
                        dbc.Input(id=f'logi-prop-input-{p}', type='text', value=SENTS[p])],
                       style={'margin-bottom': '3px'})
        for p in PROPS
    ], id='logi-props-ingroup'
)

logi_add_prem_div = html.Div([  # dbc.Card([
    dbc.Form([
        dbc.FormGroup([
            dbc.InputGroup([
                dbc.InputGroupAddon('Opérateur logique', addon_type="prepend"),
                dbc.Select(id='logi-prem-operator-select',
                           options=[
                               {'label': 'Proposition atomique', 'value': 'simple'},
                               {'label': 'Implication', 'value': 'if'},
                               {'label': 'Conjonction', 'value': 'and'},
                               {'label': 'Disjonction', 'value': 'or'},
                           ],
                           value='simple')
            ], style={'padding-right': '24px'}),
        ]),
        dbc.FormGroup([
            dbc.Label(id='logi-prem-operator-label-1', style={'padding-right': '3px', 'min-width': '20px'}),
            dbc.Select(id='logi-prem-prop-1', style={'max-width': '100px'},
                       options=[
                           {'label': p, 'value': p} for p in PROPS_WITH_NEG
                       ],
                       value=''),
            dbc.Label(id='logi-prem-operator-label-2',
                      style={'padding-right': '3px', 'padding-left': '3px', 'min-width': '20px'}),
            dbc.Select(id='logi-prem-prop-2', style={'max-width': '100px'},
                       options=[
                           {'label': p, 'value': p} for p in PROPS_WITH_NEG
                       ],
                       value=''),
        ], style={'min-width': '250px', }),
        dbc.FormGroup([
            html.Button('Ajouter', className='logi-btn', id='logi-add-prem-btn'),
        ], style={'padding-left': '24px'}),
    ], inline=True, style={'border': 'solid', 'border-width': '1px', 'padding': '8px'}),
    # justify='start', align='start'),
])

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
], style={'padding-top': '50px', 'margin': 'auto', 'width': '80%'})

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
            logi_add_prem_div,
            logi_arg_div,
        ], style={'max-width': '720px'}),
        # dbc.Col([

        # ], xs=0, lg=2),
    ], justify='start'),
    dbc.Row([
        dbc.Col([
            logi_propositions_div
        ], lg=6),
    ]),
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


@app.callback(
    [Output('logi-prem-prop-2', 'style'),
     Output('logi-prem-operator-label-1', 'children'),
     Output('logi-prem-operator-label-2', 'children')],
    Input('logi-prem-operator-select', 'value')  # , prevent_initial_call=True
)
def update_add_prem(operator):
    if operator == 'if':
        r, label_1, label_2 = {'display': '', 'max-width': '100px'}, 'Si', 'alors'
    elif operator == 'and':
        r, label_1, label_2 = {'display': '', 'max-width': '100px'}, '', 'et'
    elif operator == 'or':
        r, label_1, label_2 = {'display': '', 'max-width': '100px'}, '', 'ou'
    else:
        r, label_1, label_2 = {'display': 'none', 'max-width': '100px'}, '', ''
    return r, label_1, label_2


@app.callback(
    [Output('logi-arg-prems-div', 'children'),
     Output('logi-arg-json-div', 'children')],
    Input('logi-add-prem-btn', 'n_clicks'),
    [State('logi-prem-prop-1', 'value'),
     State('logi-prem-prop-2', 'value'),
     State('logi-prem-operator-select', 'value'),
     State('logi-arg-prems-div', 'children'),
     State('logi-arg-json-div', 'children')], prevent_initial_call=True
)
def add_premise(n_c, p1, p2, operator, premises, prems_json):
    j = json.loads(prems_json)
    assert (p1[-1] in PROPS) and ((p2 == '' and operator == 'simple') or p2[-1] in PROPS), 'Invalid premise error!'

    if operator == 'if':
        s = f'Si {p1}, alors {p2}'
        f = f'{fn(p1)} >> {fn(p2)}'
    elif operator == 'and':
        s = f'{p1} et {p2}'
        f = f'{fn(p1)} & {fn(p2)}'
    elif operator == 'or':
        s = f'{p1} ou {p2}'
        f = f'{fn(p1)} | {fn(p2)}'
    else:
        s = f'{p1}'
        f = f'{fn(p1)}'
    j['premises'].append(f)

    return premises + [html.Div(html.H5([f'P{len(premises) + 1} - ', s]))], json.dumps(
        j)  # state and update json-div with new prem


@app.callback(
    [Output('logi-result', 'children'),
     Output('logi-result-text', 'children')],
    Input('logi-eval-btn', 'n_clicks'),
    [State('logi-arg-json-div', 'children'),
     State('logi-conc-select', 'value'),
     State('logi-props-ingroup', 'children')], prevent_initial_call=True
)
def eval_argument(n_c, prems, conc, props):
    assert conc[-1] in PROPS, 'Invalid conclusion error!'

    sent_mapping = {prop['props']['children'][1]['props']['id'][-1]: prop['props']['children'][1]['props']['value'] for
                    prop in props}
    prems = json.loads(prems)['premises']
    conc = fn(conc)
    allowed_vars = {f'{v}': v for v in vars(*PROPS)}

    if eval(' & '.join(f'({p})' for p in prems), allowed_vars).is_contradiction():
        result = 'Les prémisses sont contradictoires!'
    else:
        arg = ArgumentForm(*(eval(p, allowed_vars) for p in prems), conclusion=eval(conc, allowed_vars))
        result = 'Argument déductivement valide!' if arg.is_valid() else 'Argument déductivement invalide :('

    t = arg_to_text(prems, conc, sent_mapping)

    return result, t


@app.callback(
    Output('logi-modal', 'is_open'),
    [Input('logi-modal-btn', 'n_clicks')],
    [State('logi-modal', 'is_open')],
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open
