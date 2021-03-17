"""This an about tab

works as any other tab but contains text about the project, authors, etc.
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from tools.factories import jumbotron_from_title_paragraphs
from data.markdowns import CONTRIBUTORS_MARKDOWN_TEXT, PROJECT_DETAILS_MARKDOWN


j_title = 'Project name'
j_text = ['Quick project description text']
about_jumbotron = jumbotron_from_title_paragraphs(j_title, j_text)

project_card = dbc.Card([
    dbc.CardHeader('Project details or something', className='lead'),
    dbc.CardBody(dcc.Markdown(PROJECT_DETAILS_MARKDOWN))
])


contributors_card = dbc.Card([
    dbc.CardHeader('Contributors', className='lead'),
    dbc.CardBody(dcc.Markdown(CONTRIBUTORS_MARKDOWN_TEXT))
])


# tab container, which is imported by tabindex
# divided in rows with dbc.Row()
# rows typically one or many cards, split by cols
# self contained cards may be placed in a separate file and imported
about_tab_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            about_jumbotron,
        ])
    ]),

    dbc.Row([
        dbc.Col([project_card], width=6),
        dbc.Col([contributors_card], width=3),
        #dbc.Col([], width=1)
    ], justify='around'),
], fluid=True, id='example-tab')

