from flask import Flask, jsonify
import numpy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,inspect
from sqlalchemy import Integer, Column, Float, String  
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app = Flask(__name__)
@app.route("/")
def index():
    return (
        f"Available Routes:<br/>"
        f"<a href='api/v1.0/precipitation'>Precipitation</a><br/>"
        f"<a href='api/v1.0/stations'>List of Stations</a><br/>"
        f"<a href='api/v1.0/tobs'>Temperature</a><br/>"
        f"<a href='api/v1.0/startdate'>Temperature from the start date</a><br/>"
        f"<a href='api/v1.0/start_to_end'>Temperature from start to end date</a><end>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    return f"test text precipitation"
@app.route("/api/v1.0/stations")
def stations():
    return f"test text - stations"
@app.route("/api/v1.0/tobs")
def tobs():
    return f"test text - tobs."
@app.route("/api/v1.0/startdate")
def startdate():
    return f"test text - startdate"
@app.route("/api/v1.0/start_to_end")
def start_to_end():
    return f"test text - start_to_end"
# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)