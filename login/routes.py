from flask import request, render_template
from login import login
from app import db
from app.models import Login

@login.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # pass
        username = request.form.get("username")
        password = request.form.get("password")
        loginobj = Login(username, password)
        db.session.add(loginobj)
        db.session.commit()
        print(f"{username} added...")


    return render_template ("login.html")
