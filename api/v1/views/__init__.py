from flask import Blueprint


app_views = Blueprint('apps_views', __name__, url_prefix='/api')
from views.divisas import *