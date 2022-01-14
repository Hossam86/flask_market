from enum import unique
from pydoc import describe
from unicodedata import name
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Item(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    describtion = db.Column(db.String(length=1024), nullable=False, unique=True)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'laptop', 'barcode': '893212299897', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '893212299897', 'price': 150}
    ]

    return render_template('market.html', items=items)
