# Flask
from flask import Flask
# Sqlite
from sqlalchemy import create_engine
# Views
from views import app_views
# Utiles
from  dotenv  import  load_dotenv 
from os import getenv

load_dotenv(verbose=True)
db_connect = create_engine('sqlite:///mock_data_db/mock_data.db')
#Instace Class
app = Flask(__name__)
app.register_blueprint(app_views)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = '5000'
    if getenv('API_HOTS'):
        host = getenv('API_HOTS')
    if getenv('API_POTR'):
        port = getenv('API_PORT')

    print(getenv('API_POTR'))

    app.run(host=host, port=port, threaded=True)
