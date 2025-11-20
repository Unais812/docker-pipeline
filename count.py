# this imports the flask image from the module flask to use in the code 
import os
from flask import Flask, render_template, redirect, url_for
import redis

redis_host=os.getenv('REDIS_HOST','redis')
redis_port=int(os.getenv('REDIS_PORT',6379))

app = Flask(__name__)
db = redis.Redis(host=redis_host, port=redis_port)  # <-- changed from localhost

@app.route('/')
def index():
    visits = db.incr('visits')  # increment visit count
    return render_template("index.html", visits=visits)

@app.route('/count')
def store_count():
    visits = db.incr('visits')
    return f"This page has been visited {visits} times."

@app.route('/refresh')
def refresh():
    return redirect(url_for('welcome_page'))

# New route: about page
@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)  # <-- use 0.0.0.0 for container