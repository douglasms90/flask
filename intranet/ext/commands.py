import click
from intranet.ext.database import db
from intranet.ext.auth import create_user
from intranet.models import Booking
from datetime import datetime


def createdb():
    """Create database"""
    db.create_all()

def dropdb():
    """Clean database"""
    db.drop_all()

def insertdb():
    """Insert db with sample data"""
    data = [
        Booking(id=1, dt=datetime(2026, 1, 2, 8, 0)),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Booking.query.all()

def updatedb():
    """Update to database"""
    db.session.bulk_update_mappings(Booking, [
        {'id':'1','nm':'Douglas'},
        {'id':'2','nm':'Marilza'},
        {'id':'3','nm':'Daiana'},
    ])
    db.session.commit()

def deletedb():
    db.session.delete(
        Act.query.filter_by(id=833).first())
    db.session.commit()

def init_app(app):
    # add multiple commands in a bulk
    for command in [createdb, dropdb, insertdb, updatedb, deletedb]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
