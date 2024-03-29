# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, current_app, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash
import json
from . import auth
from ..models import db, User


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html", level='SUCCESS')
    else:
        username = request.form['username']
        password = request.form['password']
        try:
            user = User.query.filter_by(username=username).first()
        except Exception as e:
            current_app.logger.error(e)
            flash("Inner Error!Something Wrong with Database!")
            return render_template("login.html", level='ERROR')
        if user is not None and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for("index.dashboard"))
        else:
            flash("Wrong Username or Password!")
            return render_template("login.html", level='ERROR')


@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('user_id')
    flash("Logout Successfully!")
    return redirect(url_for("auth.login"))


@auth.route('/register', methods=['POST'])
def register():
    username = request.values.get('username')
    password = request.values.get('password')
    confirm = request.values.get('confirm')
    email = request.values.get('email')
    if not all([username, password, confirm, email]):
        return json.dumps({'failed': 'Fill all the items first!'})
    if password == confirm:
        try:
            new_user = User(username=username, password=generate_password_hash(password), email=email)
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            return json.dumps({'failed': 'Register failed!'})
        return json.dumps({'success': 'Register Successful!'})
    else:
        return json.dumps({'failed': 'Register failed!'})
