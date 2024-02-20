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
        Atv(id=102,tp='rf',nm='slc-29',pm=12874.14,qt=1.31,rc='',pa=18791.8),
        Atv(id=103,tp='rf',nm='lci-24',pm=1000.0,qt=20.0,rc='',pa=21255.94),
        Atv(id=104,tp='rf',nm='cdb-24',pm=1000.0,qt=10.0,rc='',pa=12317.62),
        Atv(id=105,tp='rf',nm='pre-25',pm=738.14,qt=3.38,rc='',pa=3107.03),
        Atv(id=106,tp='rf',nm='inf-26',pm=3146.81,qt=0.79,rc='',pa=2906.86),
        Atv(id=107,tp='rf',nm='inf-45',pm=1291.22,qt=17.39,rc='',pa=22138.33),
        Atv(id=201,tp='fundos-imobiliarios',nm='irdm11',pm=107.59,qt=37.0,rc='N',pa=87.0),
        Atv(id=202,tp='fundos-imobiliarios',nm='mcci11',pm=98.47,qt=15.0,rc='',pa=94.0),
        Atv(id=203,tp='fundos-imobiliarios',nm='recr11',pm=94.62,qt=20.0,rc='N',pa=94.0),
        Atv(id=204,tp='fundos-imobiliarios',nm='vgip11',pm=89.33,qt=15.0,rc='',pa=0.0),
        Atv(id=205,tp='fundos-imobiliarios',nm='btlg11',pm=102.39,qt=17.0,rc='',pa=113.0),
        Atv(id=206,tp='fundos-imobiliarios',nm='bcff11',pm=7.99,qt=112.0,rc='N',pa=78.0),
        Atv(id=207,tp='fundos-imobiliarios',nm='hgru11',pm=127.04,qt=27.0,rc='',pa=136.0),
        Atv(id=208,tp='fundos-imobiliarios',nm='mall11',pm=91.66,qt=14.0,rc='N',pa=116.0),
        Atv(id=209,tp='fundos-imobiliarios',nm='pvbi11',pm=91.79,qt=4.0,rc='N',pa=106.0),
        Atv(id=210,tp='fundos-imobiliarios',nm='rbrp11',pm=87.01,qt=43.0,rc='N',pa=74.0),
        Atv(id=211,tp='fundos-imobiliarios',nm='vilg11',pm=116.83,qt=33.0,rc='N',pa=127.0),
        Atv(id=212,tp='fundos-imobiliarios',nm='vino11',pm=11.91,qt=205.0,rc='',pa=0.0),
        Atv(id=301,tp='acoes',nm='bbse3',pm=21.22,qt=65.0,rc='N',pa=34.0),
        Atv(id=302,tp='acoes',nm='b3sA3',pm=13.84,qt=135.0,rc='N',pa=15.0),
        Atv(id=303,tp='acoes',nm='egie3',pm=39.5,qt=10.0,rc='',pa=46.0),
        Atv(id=304,tp='acoes',nm='eztc3',pm=16.86,qt=80.0,rc='N',pa=22.0),
        Atv(id=305,tp='acoes',nm='flry3',pm=27.08,qt=84.0,rc='N',pa=19.0),
        Atv(id=306,tp='acoes',nm='itsa4',pm=8.78,qt=231.0,rc='',pa=0.0),
        Atv(id=307,tp='acoes',nm='mypk3',pm=13.04,qt=140.0,rc='N',pa=15.0),
        Atv(id=308,tp='acoes',nm='sapr4',pm=4.09,qt=423.0,rc='N',pa=26.0),
        Atv(id=309,tp='acoes',nm='vale3',pm=68.25,qt=25.0,rc='N',pa=73.0),
        Atv(id=310,tp='acoes',nm='vbbr3',pm=24.74,qt=83.0,rc='',pa=0.0),
        Atv(id=311,tp='acoes',nm='vivt3',pm=44.79,qt=33.0,rc='N',pa=54.0),
        Atv(id=312,tp='acoes',nm='wege3',pm=19.52,qt=66.0,rc='N',pa=40.0),
        Atv(id=401,tp='etfs',nm='ivvb11',pm=231.95,qt=14.0,rc='',pa=0.0),
        Atv(id=402,tp='bdrs',nm='baba34',pm=17.18,qt=85.0,rc='',pa=23.0),
        Atv(id=403,tp='bdrs',nm='disb34',pm=37.27,qt=33.0,rc='',pa=34.0),
        Atv(id=501,tp='criptomoedas',nm='btc',pm=255326.15,qt=0.01350731,rc='',pa=0.0),
        Atv(id=502,tp='criptomoedas',nm='beth',pm=14126.51,qt=0.18814654,rc='',pa=0.0),
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
