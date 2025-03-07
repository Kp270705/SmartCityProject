from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        is_admin = True if request.form.get('role') == 'admin' else False

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered!", "danger")
            return redirect(url_for('auth.register'))

        new_user = User(username=username, email=email, password=password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful!", "success")
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')
