from app import app
from flask import render_template, flash , redirect , url_for ,request
from api_parsing import get_holidays

@app.route('/')
def index():
    return render_template("html/index.html")
