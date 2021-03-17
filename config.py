from pathlib import Path
from dotenv import load_dotenv
from os import environ


# Load project settings
PROJECT_PATH = Path(__file__).parent
load_dotenv(PROJECT_PATH / '.env')
LOCAL_IP = environ.get('LOCAL_IP')
BASE_STORAGE_PATH = Path(environ.get('LOCAL_STORAGE_PATH'))
IS_PROD = environ.get('IS_PROD') == 'True'
PORT = 33


# Set paths to data files here.
DATA_PATHS = {
    'TEST_DATA_DF': PROJECT_PATH / 'data' / 'test_data_df.p'
}


# Browser tab title
PROJECT_TITLE = 'Phidash'

# Title and subtitle to display on header
HEADER_TITLE = 'Dashboard title'
HEADER_SUBTITLE = 'Dashboard subtitle'

# Name and bio of the project contributors. Displayed in About tab.
CONTRIBUTORS = {
    'Name McName': 'This person is working on something ',
    'Person Person': 'This person also contributed to the project. Here is some gibberish to see what happens'
                     ' when there is more text and multiple lines might be needed.',
    }

