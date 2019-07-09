# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, current_app, session, flash, g
from . import auth
from ..models import User


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        try:
            user = User.query.filter_by(username=username).first()
        except Exception as e:
            current_app.logger.error(e)
            flash("Inner Error!Something Wrong with Database!")
            return render_template("login.html")
        if user is not None and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for("index.dashboard"))
        else:
            flash("Wrong Username or Password!")
            return render_template("login.html")


@auth.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('user_id')
    flash("Logout Successfully!")
    return redirect(url_for("auth.login"))
