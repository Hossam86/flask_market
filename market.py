from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def helle_world():
    return render_template('home.html')


@app.route('/market')
def about_pages():
    return render_template('market.html')