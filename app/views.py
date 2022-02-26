from crypt import methods
from app import app
from flask import render_template, request
from app import api_parsing

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        pass
    return render_template("html/index.html")


# day = 10
# month = 10
# api_parsing.get_holiday_data(day, month)