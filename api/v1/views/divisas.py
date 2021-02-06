# Flsk
from flask import jsonify
# Views
from views import app_views
# Services
from services import hit_webhook
# DataBase
from server import db_connect
# Utiles
import requests
import re


@app_views.route('/exchange_value/<currency_pair>/')
def all_data_currency_pair(currency_pair):
    """Get All data of a currency pair

    @currency_pair String: receives as value the currency pairs how 'EUR-USD'
    """

    result = {}
    try:
        # Connect to DataBase
        conn = db_connect.connect()
        query = conn.execute(f'select name, date from divisas where name="{currency_pair.upper()}";')
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    except Exception as error:
        print(f'Error generate in all_data_currency_pair: {error}')
        return error

    return jsonify(result)

@app_views.route('/exchange_value/<currency_pair>/<date>')
def day_data_currency_pair(currency_pair, date):
    """Get data about one currency pair
    
    @currency_pair String: receives as value the currency pairs how 'EUR-USD'
    @date String: recive as value a date how '5-2-2021'
    """

    result = {}
    try:
        # Connect to DataBase
        conn = db_connect.connect()
        date_r = date.replace('-', '/')
        query = conn.execute(f'select name, exchange_pair from divisas where name="{currency_pair.upper()}" and date="{date_r}";')
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        if len(result.get('data')) > 0:
            hit_webhook(result['data'][0])
    except Exception as error:
        print(f'Error generate in day_data_currency_pair: {error}')
        return error

    return jsonify(result)
