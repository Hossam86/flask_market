from flask import Flask
app = Flask(__name__)

@app.route('/')
def helle_world():
    return '<h1>HELLO WORLD!</h1>'


@app.route('/about/<username>')
def about_pages(username):
    return f'<h1>This is about page of {username}</h1>'
