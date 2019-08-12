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

    return render_template('show_menus.html', main=main.name, sub=sub.name, soup=soup.name)

@app.route('/main', methods=['GET'])
def change_main():
    mains = db.session.query(Menu).filter(Menu.type=="main")
    main = mains[random.randrange(0, mains.count())]

    sub = request.args.get('sub', '')
    soup = request.args.get('soup', '')

    return render_template('show_menus.html', main=main.name, sub=sub, soup=soup)

@app.route('/sub', methods=['GET'])
def change_sub():
    subs = db.session.query(Menu).filter(Menu.type=="sub")
    sub = subs[random.randrange(0, subs.count())]

    main = request.args.get('main', '')
    soup = request.args.get('soup', '')

    return render_template('show_menus.html', main=main, sub=sub.name, soup=soup)

@app.route('/soup', methods=['GET'])
def change_soup():
    soups = db.session.query(Menu).filter(Menu.type=="soup")
    soup = soups[random.randrange(0, soups.count())]
    main = request.args.get('main', '')
    sub = request.args.get('sub', '')

    return render_template('show_menus.html', main=main, sub=sub, soup=soup.name)

