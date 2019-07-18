# -*- coding: utf-8 -*-
from flask import render_template, request, session, g
from . import index
from ..decorator import login_required



@index.route('/', methods=['GET'])
@login_required
def dashboard():
    return render_template("index.html", user=g.user)


@index.route('/analysis/nessus', methods=['GET'])
@login_required
def nessus_analysis():
    return render_template('nessus_analysis.html', user=g.user)


@index.route('/record_info', methods=['GET', 'POST'])
@login_required
def record_info():
    return render_template('record_info.html', user=g.user)


