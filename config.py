from pathlib import Path
from dotenv import load_dotenv
from os import environ


# Load project settings
PROJECT_PATH = Path(__file__).parent
load_dotenv(PROJECT_PATH / '.env')
LOCAL_IP = environ.get('LOCAL_IP')
BASE_STORAGE_PATH = PROJECT_PATH / 'data'
IS_PROD = environ.get('IS_PROD') == 'True'
PORT = 33

MARKDOWNS_PATH = BASE_STORAGE_PATH / 'markdowns'

# Set paths to data files here.
DATA_PATHS = {

}

# Browser tab title
PROJECT_TITLE = 'Portfolio - Martin Léonard'
