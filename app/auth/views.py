# -*- coding: utf-8 -*-
from flask import render_template, request
from ..models import db, User
from . import auth


@auth.route('/login', methods=['POST', 'GET'])
def login():
      if request.method == 'GET':
          return render_template("login.html")
