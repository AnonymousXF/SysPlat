# -*- coding: utf-8 -*-
from flask import render_template, request, session, g
from . import index
from ..decorator import login_required


@index.route('/', methods=['GET'])
@login_required
def dashboard():
    return render_template("index.html", user=g.user)


@index.route('/analysis/nessus', methods=['GET', 'POST'])
@login_required
def nessus_analysis():
    if request.method == 'GET':
        return render_template('nessus_analysis.html', user=g.user)
