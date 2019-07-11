# -*- coding: utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app
from app.models import db


app = create_app('dev')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    from flask_migrate import upgrade
    from app.models import User

    # upgrade
    upgrade()
    User.create_default_admin()


if __name__ == '__main__':
    manager.run()
