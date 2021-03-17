from config import CONTRIBUTORS

CONTRIBUTORS_MARKDOWN_TEXT = ''.join(f'### {contri}  \n{desc}  \n \n' for contri, desc in CONTRIBUTORS.items())

PROJECT_DETAILS_MARKDOWN = '### Section 1  \nSection 1 text, blablabla.  \n  \n' \
                           '### Section 2  \nSection 2 text, blablabla.  \n  \n'



