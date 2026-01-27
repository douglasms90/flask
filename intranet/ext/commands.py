import click
from intranet.ext.database import db
from intranet.ext.auth import create_user
from intranet.models import Booking, Assets
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
        Assets(id=101, cl="tesouro", nm="cxtrb", pr=101.5797, pm=98.4251, qt=100, dv=None, pl=None, vp=None),
        Assets(id=102, cl="tesouro", nm="tesouro-selic-2031", pr=18136.1 , pm=15916.69 , qt=1, dv=None, pl=None, vp=None),
        Assets(id=103, cl="rf", nm="LCI-26", pr=1119.243, pm=1000, qt=20, dv=None, pl=None, vp=None),
        Assets(id=104, cl="tesouro", nm="tesouro-ipca-2026", pr= 4341.74, pm=3146.8101, qt= 0.79, dv=None, pl=None),
        Assets(id=105, cl="tesouro", nm="tesouro-ipca-2045", pr= 1198.08, pm=1243.3294, qt=35.55, dv=None, pl=None),
        Assets(id=201, cl="fundos-imobiliarios", nm="kncr11", pr=106.31, pm=95.66, qt=17, dv= 14.53, pl=None, vp=1.04),
        Assets(id=202, cl="fundos-imobiliarios", nm="mcci11", pr=92.79, pm=93.48, qt=40, dv=11.4, pl=None, vp=0.98),
        Assets(id=203, cl="fundos-imobiliarios", nm="rbrr11", pr=89.95, pm=79.95, qt=20, dv=10.6, pl=None, vp=0.96),
        Assets(id=204, cl="fundos-imobiliarios", nm="bthf11", pr=9.35, pm=9.33, qt=600, dv= 1.123, pl=None, vp=0.91),
        Assets(id=205, cl="fundos-imobiliarios", nm="btlg11", pr=102.7, pm= 101.21, qt=40, dv=9.4101, pl=None, vp= 1),
        Assets(id=206, cl="fundos-imobiliarios", nm="hglg11", pr=157.4, pm= 149.55, qt=10, dv=13.2, pl=None, vp=0.94),
        Assets(id=207, cl="fundos-imobiliarios", nm="hgru11", pr=132.03, pm=123.62, qt=40, dv= 12.25, pl=None, vp=1.02),
        Assets(id=208, cl="fundos-imobiliarios", nm="pmll11", pr=104.34, pm=94.27, qt=40, dv= 10.25, pl=None, vp=0.89),
        Assets(id=209, cl="fundos-imobiliarios", nm="pvbi11", pr=81.8, pm= 84.79, qt=60, dv= 5.8, pl=None, vp=0.76),
        Assets(id=210, cl="fundos-imobiliarios", nm="rbrp11", pr=55.8, pm= 73.48, qt=70, dv=4.82, pl=None, vp=0.68),
        Assets(id=211, cl="fundos-imobiliarios", nm="vilg11", pr=102.85, pm=111.2, qt=40, dv=8.39, pl=None, vp=0.91),
        Assets(id=301, cl="acoes", nm="bbas3", pr=24.28, pm=20.33, qt=300, dv=1.1829, pl= 8.75, vp=0.76),
        Assets(id=302, cl="acoes", nm="bbse3", pr=36.99, pm=21.22, qt=65, dv=4.2623, pl= 8.22, vp=5.75),
        Assets(id=303, cl="acoes", nm="itsa4", pr=13.36, pm=8.34, qt=245, dv=1.7695, pl= 9.42, vp=1.62),
        Assets(id=304, cl="acoes", nm="petr4", pr=35.04, pm=29.55, qt=50, dv=3.2724, pl= 5.83, vp=1.07),
        Assets(id=305, cl="acoes", nm="sapr4", pr=8.87, pm=4.09, qt=423, dv=0.3994, pl= 6.29, vp=1.11),
        Assets(id=306, cl="acoes", nm="vale3", pr=85.02, pm=59.33, qt=100, dv= 7.619, pl=12.78, vp=1.77),
        Assets(id=400, cl="dollar", nm="cash", pr=911.52, pm=911.52, qt=1, dv=None, pl=None),
        Assets(id=401, cl="rf/eua", nm="bonds", pr=1025, pm=1052.3, qt=1, dv=None, pl=None ),
        Assets(id=402, cl="etf/eua", nm="ibit", pr=51.33, pm=49.9, qt=20, dv=None, pl=None),
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
