
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"

@app.route('/users')
def users(username):
    return f"Hello, {username}!"

@app.route('/users/<username>')
def about(username):
    return f" This is the about page for {username}."


@app.route('/contact')
def contact():
    return "This is the contact page."



if __name__ == '__main__':
    app.run(debug=True)
 