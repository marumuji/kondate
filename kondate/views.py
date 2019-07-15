from flask import request, redirect, url_for, render_template, flash
from kondate import app, db
from kondate.models import Menu
import random

@app.route('/')
def show_menus():
    return render_template('show_menus.html')

@app.route('/get', methods=['GET'])
def get_menus():
    mains = db.session.query(Menu).filter(Menu.type=="main")
    subs = db.session.query(Menu).filter(Menu.type=="sub")
    soups = db.session.query(Menu).filter(Menu.type=="soup")

    main = mains[random.randrange(0, mains.count())]
    sub = subs[random.randrange(0, subs.count())]
    soup = soups[random.randrange(0, soups.count())]

    return render_template('show_menus.html', main=main, sub=sub, soup=soup)

import random
