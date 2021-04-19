import dash
import pickle
import dash_bootstrap_components as dbc
import codecs

from config import PROJECT_TITLE, IS_PROD, MARKDOWNS_PATH

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX], title=PROJECT_TITLE,
                suppress_callback_exceptions=IS_PROD)


# Load data
def load_df_from_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def load_markdown_file(filename, path=MARKDOWNS_PATH):
    with codecs.open(path / filename, 'r', 'utf-8') as f:
        return f.read()


COURS_MD = load_markdown_file('cours.md')
PRES_MD = load_markdown_file('pres.md')
MAT_MD = load_markdown_file('materiel.md')
SEQ_MD = load_markdown_file('seq.md')
AUTH_MD = load_markdown_file('auth.md')
CONSPI_MD = load_markdown_file('conspi.md')
GRILLE_MD = load_markdown_file('grille.md')
QUESTIONNAIRE_MD = load_markdown_file('questionnaire.md')
LOGI_MD = load_markdown_file('logi.md')
LOGI_INST_MD = load_markdown_file('logi_inst.md')


