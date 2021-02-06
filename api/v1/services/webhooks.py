# Utils
import requests
from  dotenv  import  load_dotenv 
from os import getenv

load_dotenv(verbose=True)
webhook_url = getenv('WEBHOOK_URL')


def hit_webhook(data):
    """hit_webhook

    @data dict: receives a dictionary with info consulted in the database
    """
    try:
        print(webhook_url, data)
        response = requests.post(webhook_url, data)
        print(response)
        return response
    except Exception as error:
        print(f'Error send_post_webhook: {error}')
        return error
