var earthquake_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
var plate_url = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json"


function markerSize(magnitude) {
    return magnitude * 4;
};

var earthquake = new L.LayerGroup();

