from flask import Flask, Blueprint
register = Blueprint('register', __name__, template_folder='templates', static_url_path='/static', static_folder='static')
from register import routes

