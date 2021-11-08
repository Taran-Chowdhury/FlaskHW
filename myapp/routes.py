from myapp import myapp_obj
from myapp.forms import TopCitiesForm
from flask import render_template, flash, redirect

from myapp import db
from myapp.models import TopCity

@myapp_obj.route("/", methods = ['GET',"POST"])
def home():
    form = TopCitiesForm()

    if form.validate_on_submit():
        city = TopCity(city_name = form.city_name.data, city_rank = form.city_rank.data, visited = form.visited.data)
        db.session.add(city)
        db.session.commit()

    top_cities = TopCity.query.order_by(TopCity.city_rank).all()
    title = 'Top Cities'
    name = 'Taran'
    return render_template('home.html', title = title, name = name, top_cities = top_cities, form = form)
