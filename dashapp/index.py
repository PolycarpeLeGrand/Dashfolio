import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash

from dashapp import app
from dashapp.home.hometab import home_tab_layout
from dashapp.material.materialtab import material_tab_layout
from dashapp.phi101.phi101tab import phi101_tab_layout
from dashapp.phi102.phi102tab import phi102_tab_layout
from dashapp.logi.logitab import logi_tab_layout

from config import PROJECT_TITLE

# Register tabs following this format
# {'name': 'tab-X', 'ulr': '/tabname', 'label': 'Tab Name', 'container': this_tab_layout}
TABS = [
    {'name': 'tab-0', 'url': '/accueil', 'label': 'Accueil', 'container': home_tab_layout},
    {'name': 'tab-1', 'url': '/materiel', 'label': 'Exemples de matériel', 'container': material_tab_layout},
    {'name': 'tab-2', 'url': '/101', 'label': 'Philosophie et rationalité', 'container': phi101_tab_layout},
    {'name': 'tab-3', 'url': '/102', 'label': 'L\'être humain', 'container': phi102_tab_layout},
    {'name': 'tab-4', 'url': '/logi', 'label': 'Logique et argumentation', 'container': logi_tab_layout},
]

BG_COLOR = '#255c60'

# Builds tabs from TABS. Don't touch.
tabs = dbc.Tabs(
    [dbc.Tab(label=tab['label'], label_style={'cursor': 'pointer', 'padding': '10px', 'color': 'white'}, active_label_style={'color': 'white', 'background': BG_COLOR, 'border': '1px', 'border-color': BG_COLOR, 'border-style': 'solid'}) for tab in TABS],
    id='tabs', active_tab='tab-0', style={'padding-left': '10px', 'border': '0px'}, className='lead'
)


layout = html.Div([
    dcc.Location(id='url', refresh=False, pathname=TABS[0]['url']),
    # header,
    html.Div([
        dbc.Row([
            dbc.Col(html.H1(PROJECT_TITLE, style={'text-align': 'center', 'padding': '5px 20px 0px 30px', 'margin': '0px'}), width='auto'),
            dbc.Col(tabs),
        ], no_gutters=True, ),
    ], className='pt-2 text-light bg-dark', ),#style={'border-bottom-style': 'solid', 'border-width': '0px'}),
    dbc.Container([], id='tab-container', fluid=True, style={'padding-top': '3vh', 'padding-bottom': '3vh'}),
], style={'font-family': 'helvetica,arial,courier,sans-serif'})


@app.callback(
    [Output(component_id='tab-container', component_property='children'),
     Output(component_id='tabs', component_property='active_tab'),
     Output(component_id='url', component_property='pathname'),],
    [Input(component_id='tabs', component_property='active_tab'),
     Input(component_id='url', component_property='pathname')]
)
def update_tab(selected_tab, curr_url):
    """Updates selected tab and tab container on url update"""

    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    tab = next(filter(lambda x: x['name'] == selected_tab, TABS)) if trigger_id == 'tabs' else \
        next(filter(lambda x: x['url'] == curr_url, TABS))

    return tab['container'], tab['name'], tab['url']

