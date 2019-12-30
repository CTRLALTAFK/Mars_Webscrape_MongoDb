from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mars-webscrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
    ____ = mongo.db.____.find_one()
    return render_template("index.html", ____=____)


@app.route("/scrape")
def scraper():
    ___ = mongo.db.___
    ____data = Mars_webscrape.scrape()
    ___.update({}, ____data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
