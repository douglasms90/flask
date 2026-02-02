from flask import abort, render_template, request, redirect, url_for
from intranet.models import Booking, Assets, CommandForm
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
    form = CommandForm()
    assets = Assets.query.order_by(Assets.id).all()
    if form.validate_on_submit():
        if form.msg.data == "sync":
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
            return redirect(url_for("webui.assets"))

        else:
            pass
    data = list()
    tt = ta = 0
    dols = 5.2
    for asset in assets:
        ta += asset.pm * asset.qt if not str(asset.id).startswith("4") else (asset.pm * asset.qt) * dols
        tt += asset.pr * asset.qt if not str(asset.id).startswith("4") else (asset.pr * asset.qt) * dols
        data.append({
            "id":f"{asset.id}",
            "cl":f"{asset.cl}",
            "nm":f"{asset.nm.upper()}",
            "v%":f"{((asset.pr-asset.pm)/asset.pr)*100:.2f}%",
            "pr":f"{asset.pr:.2f}",
            "pm":f"{asset.pm:.2f}",
            "qt":f"{asset.qt}",
            "d%":f"{(asset.dv/asset.pr)*100:.2f}%" if asset.dv is not None else "",
            "y%":f"{(asset.dv/asset.pm)*100:.2f}%" if asset.dv is not None else "",
            "pl":f"{asset.pl}" if asset.pl is not None else "",
            "vp":f"{asset.vp}" if asset.vp is not None else "",
            "ps":f"{(asset.pr*asset.qt if not str(asset.id).startswith("4") else (asset.pr*asset.qt) * dols):.2f}",
            "va":f"{(asset.pm*asset.qt if not str(asset.id).startswith("4") else (asset.pm*asset.qt) * dols):.2f}",
            "rs":f"{(asset.pr*asset.qt)-(asset.pm*asset.qt):.2f}",
            "tt":f"{tt:.2f}",
            "ta":f"{ta:.2f}"
        })
    return render_template("assets.html", data=data, form=form)
