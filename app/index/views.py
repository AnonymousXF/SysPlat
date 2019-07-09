# -*- coding: utf-8 -*-
from flask import render_template, session, g
from . import index


@index.route('/', methods=['GET'])
def dashboard():
    return render_template("index.html", user=g.user)
