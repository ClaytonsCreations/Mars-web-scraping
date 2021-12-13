from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")



@app.route("/")
def home():
    scraped_data = mongo.db.collection.find_one()
    return render_template("index.html", data=scraped_data)


@app.route("/scrape")
def scrape():
    mars_scrape = mars_scraping.scrape()
    print(mars_scrape)
    mongo.db.collection.update({}, mars_scrape, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
