from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def helle_world():
    return render_template('home.html')


@app.route('/market')
def market_pages():
    items=[
        {'id':1, 'name':'Phone', 'barcode':'893212299897', 'price':500},
        {'id':2, 'name':'laptop', 'barcode':'893212299897', 'price':900},
        {'id':3, 'name':'Keyboard', 'barcode':'893212299897', 'price':150}
    ]

    return render_template('market.html', items=items)
