from application import app
from flask import render_template

@app.route('/')
def site_index():
    return render_template('site/index.html')
