from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def helle_world():
    return render_template('home.html')


@app.route('/about/<username>')
def about_pages(username):
    return f'<h1>This is about page of {username}</h1>'