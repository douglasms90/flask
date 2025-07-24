import click
from intranet.ext.database import db
from intranet.ext.auth import create_user
from intranet.models import Booking


def createdb():
    """Create database"""
    db.create_all()

def dropdb():
    """Clean database"""
    db.drop_all()

def insertdb():
    """Insert to database"""
    db.session.bulk_save_objects([
        Booking(id=1,nm='Douglas'),
    ])
    db.session.commit()

def updatedb():
    """Update to database"""
    db.session.bulk_update_mappings(Booking, [
        {'id':'2','sn':'48575443CB5FA29F'}, # 737 738 741 763
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
