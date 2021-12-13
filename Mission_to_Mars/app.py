from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")



@app.route("/")
def index():
    mars_scrape = mongo.db.mars_scrape.find_one()
    return render_template("index.html", data=mars_scrape)


@app.route("/scrape")
def scrape():
    mars_scrape = mongo.db.mars_scrape
    scraped_data = mars_scraping.scrape()
    print(scraped_data)
    mongo.db.mars_scrape.update({}, scraped_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
