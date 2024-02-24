from intranet.ext.database import db
from intranet.models import Atv


def createdb():
    """Create database"""
    db.create_all()

def dropdb():
    """Clean database"""
    db.drop_all()

def insertdb():
    """Insert to database"""
    db.session.bulk_save_objects([
        Atv(id=101,tp='rf',nm='inback',pm=79.18,qt=1.0,rc='',pa=80.8),
    ])
    db.session.commit()

def updatedb():
    """Update to database"""
    db.session.bulk_update_mappings(Act, [
        {'id':'832','sn':'48575443CB5FA29F'}, # 737 738 741 763
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
