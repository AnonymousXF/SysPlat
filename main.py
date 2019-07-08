# -*- coding: utf-8 -*-
from flask import session, g
from app import create_app
from app.models import User

app = create_app('dev')


@app.before_request
def make_info_available():
    if 'user_id' in session:
        g.user = User.query.filter_by(id=session['user_id']).first()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
