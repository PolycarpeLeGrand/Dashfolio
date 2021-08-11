import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, MATCH, ALL
import dash
from dash.exceptions import PreventUpdate

from dashapp import app
from dashapp.home.homepage import home_layout
from dashapp.material.materialtab import material_layout
from dashapp.phi101.phi101tab import phi101_layout
from dashapp.phi102.phi102tab import phi102_layout
from dashapp.logi.logitab import logi_layout
from dashapp.lotr.lotrpage import lotr_layout

from config import PROJECT_TITLE


# Register tabs following this format
# {'name': 'tab-X', 'ulr': '/tabname', 'label': 'Tab Name', 'container': this_tab_layout}

PAGES = [
    {'name': 'tab-0', 'url': '/', 'label': 'Accueil', 'container': home_layout},
    {'name': 'tab-1', 'url': '/101', 'label': 'Philosophie et rationalité', 'container': phi101_layout},
    {'name': 'tab-2', 'url': '/102', 'label': 'L\'être humain', 'container': phi102_layout},
    {'name': 'tab-3', 'url': '/materiel', 'label': 'Exemples de matériel', 'container': material_layout},
    {'name': 'tab-4', 'url': '/logi', 'label': 'Logique et argumentation', 'container': logi_layout},
    # {'name': 'tab-5', 'url': '/philotr', 'label': 'Jeu questionnaire', 'container': lotr_layout},
]


sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2('', className="display-4")),
        #dbc.Col(
        #    html.Img(src='assets/favicon.ico', className='display-4', id='logo'),
        #    id='logo-col'
        #),
        dbc.Col(
            html.Button(
                # use the Bootstrap navbar-toggler classes to style the toggle
                html.Span(className="navbar-toggler-icon"),
                className='navbar-toggler',
                # the navbar-toggler classes don't set color, so we do it here
                style={

                },
                id="toggle",
            ),
            width="auto",
            align="center",
        ),
    ], id='header-row', no_gutters=True
)

nav_drop = dbc.DropdownMenu([
    dbc.DropdownMenuItem('Premier', href='#'),
    dbc.DropdownMenuItem('Second', href='#'),
    ],
    nav=True,
    in_navbar=True,
    label='Matos'
)

nd = dbc.Collapse(
    html.Div([
        dbc.NavLink('Poil', href='#', active='exact', id={'type': 'nav-btn', 'id': 'poil'}),
        dbc.NavLink('Allo', href='#', active='exact', id={'type': 'nav-btn', 'id': 'allo'})
    ]),
    is_open=True
)

sidebar = html.Div(
    [
        sidebar_header,
        html.Div(
            [
                # html.Hr(),
                html.P(
                    ['Martin Léonard', html.Br(), 'Enseignant en philosophie'],
                    className="lead",
                    style={'text-align': 'center'},
                    id='nav-subtitle'
                ),
                html.Hr(),
            ],
            id="blurb",
        ),
        dbc.Collapse(
            dbc.Nav(
                [dbc.NavLink(link['label'], href=link['url'], active='exact', id={'type': 'nav-btn', 'id': link['name']}) for link in PAGES], #  + [nd, dbc.NavLink('Fin', href='#', active='exact', id={'type': 'nav-btn', 'id': 'asdo'})],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
    # className='pattern-zigzag-lg'
)


layout = html.Div([
    dcc.Location(id='url'),
    sidebar,
    html.Div(id='page-content')
], id='layout-div')


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    try:
        return next(filter(lambda x: x['url'] == pathname, PAGES))['container']
    except StopIteration:
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f'Mention honoralbe à Théo Leplay'),
            ]
        )


@app.callback(
    Output("collapse", "is_open"),
    Input("toggle", "n_clicks"),
    [State("collapse", "is_open")]
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

