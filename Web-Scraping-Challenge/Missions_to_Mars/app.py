# importing Flask
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

#!pip install splinter

import pandas as pd
import json
from splinter import Browser
from bs4 import BeautifulSoup as bs
import datetime as dt
import time



# Creating an app, being sure to pass __name__
app = Flask(__name__)

# MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_db
collection = db.mars
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
#mongo = pymongo(app)

# when a user click the /index 
@app.route("/")
def index():
    datapage = collection.find_one()
    return render_template("Index.html", datapage=datapage)

# when a user click the /scrape New Data
@app.route("/scrape")
def scrape():
    collection.drop()
    scraped_data = scrape_mars.scrape_all()
    collection.insert_one(scraped_data)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)


  
