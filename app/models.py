from app import db

from datetime import datetime, timezone

class Login(db.Model):
    __tablename__ = 'users'
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    def __init__(self, username, password):
        self.username = username
        self.password = password



class Issue(db.Model):
    __tablename__ = 'issues'
    __bind_key__ = 'issues'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)  # Store category of issue
    priority = db.Column(db.Enum('low', 'medium', 'high', 'critical', name="priority_levels"), default="medium")
    issue = db.Column(db.String(500), nullable=False)  # Description of the issue
    contact = db.Column(db.String(15), nullable=True)  # Optional contact number
    latitude = db.Column(db.Float, nullable=False)  # Store latitude
    longitude = db.Column(db.Float, nullable=False)  # Store longitude
    attachment = db.Column(db.String(255), nullable=True)  # File path for uploaded image
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, category, priority, issue, contact, latitude, longitude, attachment=None):
        self.category = category
        self.priority = priority
        self.issue = issue
        self.contact = contact
        self.latitude = latitude
        self.longitude = longitude
        self.attachment = attachment


class Register(db.Model):
    __tablename__ = 'register'
    __bind_key__ = 'register'
    
    id = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(150), nullable=False)
    userName = db.Column(db.String(50), nullable=False)  
    userPassword = db.Column(db.String(50), nullable=False)
    userType = db.Column(db.String(500), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, userEmail, userName, userPassword, userType):
        self.userEmail = userEmail
        self.userName = userName
        self.userPassword = userPassword
        self.userType = userType
        