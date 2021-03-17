import dash
import pickle
import dash_bootstrap_components as dbc

from config import PROJECT_TITLE, IS_PROD, DATA_PATHS

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX], title=PROJECT_TITLE,
                suppress_callback_exceptions=IS_PROD)


# Load data
def load_df_from_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


DATA = {name: load_df_from_pickle(path) for name, path in DATA_PATHS.items()}


# DATA = [2312, 34234, 3453]  # with temp as open(): DATA = pickle.load(PATH)

