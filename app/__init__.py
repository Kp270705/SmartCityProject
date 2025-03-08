import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import uuid

# ✅ Create Flask app
app = Flask(__name__)

# ✅ Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory DB (not persistent)
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:///users.db',
    'issues': 'sqlite:///issues.db',
    'register': 'sqlite:///register.db',
    # 'login': 'sqlite:///login.db',
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'Uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}
app.secret_key = uuid.uuid4().hex
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# check file extension:
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# ✅ Initialize database
db = SQLAlchemy(app)

# ✅ Import models AFTER initializing 
from app import models

# ✅ Create tables for all binds
with app.app_context():
    db.create_all()

from app import routes
