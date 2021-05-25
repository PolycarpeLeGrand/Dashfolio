from dashapp import app
from dashapp.layout import layout

from config import LOCAL_IP, PORT, IS_PROD

app.layout = layout
server = app.server

if __name__ == '__main__':
    if IS_PROD:
        ip = LOCAL_IP
        port = PORT
        app.run_server(debug=False, host=ip, port=port)
    else:
        app.run_server(debug=True)

