from flask import abort, render_template, request, redirect, url_for
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
        return redirect(url_for("webui.assets"))
    data = list()
    tt = ta = 0
    dols = 5.2
    for asset in assets:
        ta += asset.pr*asset.qt if asset.id is not 4 else (asset.pr*asset.qt)*dols
        tt += asset.pm*asset.qt if asset.id is not 4 else (asset.pr*asset.qt)*dols
        data.append({
            "id":f"{asset.id}",
            "cl":f"{asset.cl}",
            "nm":f"{asset.nm.upper()}",
            "v%":f"{'%.2f' %(((asset.pr-asset.pm)/asset.pr)*100)}%",
            "pr":f"{'%.2f' %(asset.pr)}",
            "pm":f"{'%.2f' %(asset.pm)}",
            "qt":f"{asset.qt}",
            "d%":f"{'%.2f'%((asset.dv/asset.pr)*100) if asset.dv is not None else 0}%",
            "y%":f"{'%.2f'%((asset.dv/asset.pm)*100) if asset.dv is not None else 0}%",
            "pl":f"{asset.pl if asset.pl is not None else ""}",
            "vp":f"{asset.vp if asset.vp is not None else ""}",
            "ps":f"{'%.2f' %(asset.pr*asset.qt)}",
            "va":f"{'%.2f' %(asset.pm*asset.qt)}",
            "rs":f"{'%.2f' %((asset.pr*asset.qt)-(asset.pm*asset.qt))}",
            "tt":f"{'%.2f' %(tt)}",
            "ta":f"{'%.2f' %(ta)}"
        })
    return render_template("assets.html", data=data, form=form)
