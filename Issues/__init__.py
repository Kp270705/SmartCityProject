from flask import Flask, Blueprint
# issues = Blueprint('issues', __name__, template_folder='templates', static_url_path='/static', static_folder='static')
issues = Blueprint('issues', __name__, template_folder='templates', static_folder='static', static_url_path='/issues/static')

from Issues import routes

