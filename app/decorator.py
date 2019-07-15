# -*- coding: utf-8 -*-
from functools import wraps
from flask import session, flash, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' in session and session['user_id']:
            return f(*args, **kwargs)
        else:
            flash("Need Login First!")
            return redirect(url_for('auth.login'))
    return decorated
