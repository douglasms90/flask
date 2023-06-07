from intranet.ext.database import db
from intranet.models import Vln, Act
from datetime import datetime


def createdb():
    """Create database"""
    db.create_all()

def dropdb():
    """Clean database"""
    db.drop_all()

def populatedb():
    """Populate db with sample data"""
    data = [
        Vln(olt="OLT-SANTANESIA", tfc="0/1/14:", vln=765),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()

def init_app(app):
    # add multiple commands in a bulk
    for command in [createdb, dropdb, populatedb]:
        app.cli.add_command(app.cli.command()(command))
