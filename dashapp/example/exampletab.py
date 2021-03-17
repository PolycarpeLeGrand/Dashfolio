"""Basic tab layout

A tab's main component should be a dbc.Container or html.Div, which is added to index.py
Subcomponents and callbacks can be declared here or in submodules to keep things clean
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from tools.factories import jumbotron_2_columns
from dashapp import app

# Set tab id
TAB_ID = 'example-tab'


# Jumbotron
title = 'Example jumbo'
jum_col_1 = 'Desc text in col 1'
ex_jumbotron = jumbotron_2_columns(title, jum_col_1)


# Most content will be held in cars, that can be defined here or imported
# If cards are self contained, it's nicer to split them in individual files
ex_card_1 = dbc.Card([
    dbc.CardHeader('First card header and stuff', className='lead'),
    dbc.CardBody([
        dcc.Markdown('Card text', className='h6')
    ])
])


# tab container, which is imported by tabindex
# divided in rows with dbc.Row() and then cols with dbc.Col()
# each col typically holds one card
example_tab_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ex_jumbotron,
        ])
    ]),

    dbc.Row([
        dbc.Col([
            ex_card_1
        ], width=3),
        dbc.Col([
            # ex_card_2
        ]),
    ]),
], fluid=True, id=TAB_ID)


# callbacks go below

