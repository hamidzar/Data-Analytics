import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='api/v1.0/precipitation'>Precipitation</a><br/>"
        f"<a href='api/v1.0/stations'>List of Stations</a><br/>"
        f"<a href='api/v1.0/tobs'>Temperature</a><br/>"
        f"<a href ='/api/v1.0/<start>'>Temperature from the start date<br/>"
        f"<a href ='/api/v1.0/<start>/<end>'>Temperature from start to end date<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query measurement date and prcp
    results = session.query(Measurement.date,Measurement.prcp).all()

    # Convert to list of dictionaries to jsonify
    precipitation= []

    for date, ppt in results:
        new = {}
        new["Date"] = date
        new[date] = ppt
        precipitation.append(new)

    session.close()

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).all()

    # Create a dictionary from the row data and append to a list
    stations = []
    for station,name,lat,lon,elevation in results:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Long"] = lon
        station_dict["Elevation"] = elevation
        stations.append(station_dict)

    session.close()
 
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Get the last date contained in the dataset and date from one year ago
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    one_year_back = last_date - dt.timedelta(days=365)

    # Query for the dates and temperature values
    temper_results = (session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.date >= one_year_back).order_by(Measurement.date).all())
    session.close()

    return jsonify(temper_results)

@app.route("/api/v1.0/<start>")
def temp_start(start):
   
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    startdate_formated = dt.datetime.strptime(start,"%Y-%m-%d")
    stats_temp = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs),func.avg(Measurement.tobs))\
    .filter(Measurement.date > startdate_formated ).all()
    session.close()  
    return jsonify(max=stats_temp[0][0], min=stats_temp[0][1], avg=stats_temp[0][2])
  

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    startdate_formated = dt.datetime.strptime(start,"%Y-%m-%d")
    enddate_formated = dt.datetime.strptime(end,"%Y-%m-%d")
    if (enddate_formated < startdate_formated):
        return f"start date {start} after end date {end}"
    stats_temp = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs),func.avg(Measurement.tobs))\
    .filter(Measurement.date > startdate_formated ).filter(Measurement.date <= enddate_formated).all()
    session.close() 
    return jsonify(max=stats_temp[0][0], min=stats_temp[0][1], avg=stats_temp[0][2])

    
if __name__ == '__main__':
    app.run(debug=True)