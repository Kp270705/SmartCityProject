from flask import Flask, Blueprint

login = Blueprint('login', __name__, template_folder='templates', static_folder='static')


from login import routes

