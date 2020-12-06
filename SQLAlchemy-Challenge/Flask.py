import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='api/v1.0/precipitation'>Precipitation</a><br/>"
        f"<a href='api/v1.0/stations'>List of Stations</a><br/>"
        f"<a href='api/v1.0/tobs'>Temperature</a><br/>"
        f"Temperature from the start date:/api/v1.0/<start><br/>"
        f"Temperature from start to end date:/api/v1.0/<start>/<end>"
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
    session = Session(engine)
    Last_Date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_back = dt.date(2017,8,23) - dt.timedelta(days=365)
    temper_result =  session.query(Measurement.date,Measurement.tobs).\
                                 filter(Measurement.date >= year_back).all()
    session.close()

    return jsonify(temper_result)

@app.route("/api/v1.0/<start>")
def temp_start(start):
   
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    big_list = []
    for date, min, avg, max in results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["TMIN"] = min
        tobs_dict["TAVG"] = avg
        tobs_dict["TMAX"] = max
        big_list.append(tobs_dict)

    session.close()    

    return jsonify(big_list)

@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()
    
    big_list = []
    for date, min, avg, max in results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["TMIN"] = min
        tobs_dict["TAVG"] = avg
        tobs_dict["TMAX"] = max
        
        big_list.append(tobs_dict)

    session.close()    

    return jsonify(big_list)      


if __name__ == '__main__':
    app.run(debug=True)