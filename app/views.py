from app import app
from flask import render_template, flash , redirect , url_for ,request

@app.route('/')
def index():
    return render_template("html/index.html")