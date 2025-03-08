from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from app.models import Register
from app import db
from register import register

bcrypt = Bcrypt()


@register.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        userType = request.form.get('userType')

        new_user = Register(email, username, password, userType)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful!", "success")
        # return redirect(url_for('auth.login'))
    
    return render_template('register.html')
