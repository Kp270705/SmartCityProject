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
    issue = db.Column(db.String(500), nullable=False)  # Description of the issue
    attachment = db.Column(db.String(255), nullable=True)  # File path for uploaded image
    priority = db.Column(db.Enum('low', 'medium', 'high', 'critical', name="priority_levels"), default="medium")
    latitude = db.Column(db.Float, nullable=False)  # Store latitude
    longitude = db.Column(db.Float, nullable=False)  # Store longitude
    category = db.Column(db.String(50), nullable=False)  # Store category of issue
    contact = db.Column(db.String(15), nullable=True)  # Optional contact number
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, issue, latitude, longitude, category, attachment=None, priority="medium", contact=None):
        self.issue = issue
        self.latitude = latitude
        self.longitude = longitude
        self.category = category
        self.attachment = attachment
        self.priority = priority
        self.contact = contact