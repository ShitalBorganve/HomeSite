#!/usr/bin/env python

from flask import render_template, url_for
from app import app, db, models
from random import choice

@app.route('/')
@app.route('/index')
def index():
    paintings = models.Painting.query.all()
    painting = choice(paintings)
    return render_template('images.html', painting=painting)

@app.route('/images')
def images():
    pics = ['Donquixote.jpg', 'Monalisa.jpg', 'Starrynight.jpg']
    return \
"""
<meta http-equiv="refresh" content="5">
<img src='%s' style='width:auto;max-height:100%%;'>
""" % url_for('static', filename=choice(pics))
