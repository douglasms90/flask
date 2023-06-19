from intranet.ext.database import db
from intranet.models import Vln, Act
from datetime import datetime


def createdb():
    """Create database"""
    db.create_all()

def dropdb():
    """Clean database"""
    db.drop_all()

def insertdb():
    """Insert database"""
    db.session.bulk_save_objects([
        Vln(olt="OLT-SANTANESIA", tfc="0/1/14:", vln=765),
    ])
    db.session.commit()

def updatedb():
    """Update db with sample data"""
    db.session.bulk_update_mappings(Act, [
        {id:490, req:'OLT: OLT-ARROZAL --- Interface: 0/6/10: CAIXA - K - Jd. AMALIA 2 (CONDOMINIO) ---- SN: 6485754436CD035A6 67179 K07', sn:'485754436CD035A6'},
        {id:492, req:'OLT: OLT-PIRAI-AFRODITE --- Interface: 0/17/10: CAIXA K - RIBEIRAO DAS LAJES ---- SN:48575443016664A4 67146 K06', sn:'48575443016664A4'},
        {id:502, req:'OLT: OLT-PIRAI-AFRODITE --- Interface: 0/19/4: CAIXA - E (ASILO) - AREA 11 ---- SN: 48575443E1B241A4 26680 E02'},
        {id:504, req:'OLT: OLT-PIRAI-AFRODITE --- Interface: 0/19/8: CAIXA - I (ASILO) - AREA 09 ---- SN: 485754435CD63EA7 44057 I11', sn:'485754435CD63EA7'},
    ])
    db.session.commit()

def init_app(app):
    # add multiple commands in a bulk
    for command in [createdb, dropdb, insertdb, updatedb]:
        app.cli.add_command(app.cli.command()(command))
