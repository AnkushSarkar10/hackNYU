# from crypt import methods
from app import app, api_parsing
from flask import render_template, request, url_for
from datetime import datetime

@app.route('/')
def index():
    if request.method == "POST":
        pass
    return render_template("html/index.html")

@app.route('/results', methods=["GET","POST"])
def results():
    if request.method == "POST":
        # name = request.form.get("name")
        date = request.form.get("date")
        date_obj = datetime.strptime(date,"%Y-%m-%d")
        day = date_obj.day
        month = date_obj.month

        data = api_parsing.get_holiday_data(day, month)
        # data = {'India': ['Mahatma Gandhi Jayanti', 'Maha Saptami'], 'China': ['National Day Golden Week holiday'], 'Germany': ['Harvest Festival'], 'Australia': ['Daylight Saving Time starts']}
        return render_template("html/new_results.html",data=data)


# day = 10
# month = 10
# api_parsing.get_holiday_data(day, month)