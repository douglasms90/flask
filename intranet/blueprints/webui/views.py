from flask import abort, render_template, request
from intranet.models import Booking, Assets, SyncForm
from intranet.ext.webscraping import bs
from intranet.ext.database import db
from collections import defaultdict

def index():
    bookings = Booking.query.order_by(Booking.dt).all()
    grouped_bookings = defaultdict(list)
    for booking in bookings:
        day = booking.dt.date()  # extrai apenas a data
        grouped_bookings[day].append(booking)
    return render_template("index.html", grouped_bookings=grouped_bookings)

def booking(booking_id):
    booking = Booking.query.filter_by(id=booking_id).first() or abort(404, "horário nao encontrado")
    return render_template("booking.html", booking=booking)

def assets():
    msg = None
    form = SyncForm()
    assets = Assets.query.order_by(Assets.id).all()
    titles = ['ID', 'CL', 'NM', 'PR', 'PM', 'QT', 'DV', 'PL', 'VP']
    if form.validate_on_submit():
        for i in assets:
            print(i.cl)
            if i.cl == 'rf':
                pass
            elif i.cl == 'dollar':
                pass
            elif i.cl == 'rf/eua':
                pass
            else:
                st = bs(f"https://statusinvest.com.br/{i.cl}/{i.nm}")
                pr = float((st.find_all('strong', class_='value')[0].text).replace('.', '').replace(',', '.'))
                Assets.query.filter_by(id=i.id).update({"pr":pr})
                if i.cl == 'fundos-imobiliarios':
                    dv = float((st.find_all('span', class_='sub-value')[3].text)[3:].replace(',', '.'))
                    try:
                        vp = float(st.find_all('strong', class_='value')[6].text.replace(',', '.'))
                    except:
                        vp = 0
                    Assets.query.filter_by(id=i.id).update({"dv":dv,"vp":vp})
                if i.cl == 'acoes':
                    dv = float((st.find_all('span', class_='sub-value')[3].text)[3:].replace(',', '.'))
                    pl = float(st.find_all('strong', class_='value d-block lh-4 fs-4 fw-700')[1].text.replace(',', '.'))
                    vp = float(st.find_all('strong', class_='value d-block lh-4 fs-4 fw-700')[3].text.replace(',', '.'))
                    Assets.query.filter_by(id=i.id).update({"dv":dv,"pl":pl, "vp":vp})
        db.session.commit()
        return render_template("assets.html", assets=assets, form=form)
    return render_template("assets.html", titles = titles, assets=assets, form=form)
