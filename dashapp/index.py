import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
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
    {'name': 'tab-0', 'url': '/', 'label': 'Accueil', 'container': home_tab_layout},
    {'name': 'tab-1', 'url': '/materiel', 'label': 'Exemples de matériel', 'container': material_tab_layout},
    {'name': 'tab-2', 'url': '/101', 'label': 'Philosophie et rationalité', 'container': phi101_tab_layout},
    {'name': 'tab-3', 'url': '/102', 'label': 'L\'être humain', 'container': phi102_tab_layout},
    {'name': 'tab-4', 'url': '/logi', 'label': 'Logique et argumentation', 'container': logi_tab_layout},
]


nav_items = [dbc.NavItem(dbc.NavLink(t['label'], href=t['url'], active='exact', style={'color': 'white'})) for t in TABS]

navbar = dbc.Navbar([
    html.H2(PROJECT_TITLE, style={'text-align': 'center', 'padding': '10px 80px 0px 30px', 'margin': '0px', 'color': 'white'}),
    dbc.NavbarToggler(id="navbar-toggler"),
    dbc.Collapse(nav_items, style={'padding-top': '5px'}, id="navbar-collapse", navbar=True),
], color='black', dark=True, sticky='top', expand='lg', style={'padding': '0px', 'border': 'none'})


layout = html.Div([
    dcc.Location(id='url', refresh=False, pathname=TABS[0]['url']),
    navbar,
    dbc.Container([], id='tab-container', fluid=True, style={'padding-top': '3vh', 'padding-bottom': '3vh'}),
], style={'font-family': 'helvetica,arial,courier,sans-serif'})


@app.callback(
    Output('tab-container', 'children'),
    [Input('url', 'pathname')]
)
def update_page(pathname):
    return next(filter(lambda x: x['url'] == pathname, TABS))['container']


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open