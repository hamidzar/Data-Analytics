var myMap = L.map("map", {
  center: [37.8968, -119.5828],
  zoom: 3.5,
  });
console.log("Welcome to Map Creation")

// Title layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

/ Link for the geojson data.
var geodata_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Fetching the data 
d3.json(geodata_url, function(data) {
    console.log("Inside function to grab geojson data")

    // functions for calculating the color and radius.
  function styleInfo(feature) {
    return {
      opacity: 1,
      fillOpacity: 1,
      fillColor: getColor(feature.properties.mag),
      color: "#000000",
      radius: getRadius(feature.properties.mag),
      stroke: true,
      weight: 0.5
    };
  }

  // Function for Color of the marker related to the magnitude of the earthquake.
  function getColor(magnitude) {
    switch (true) {
      case magnitude > 5:
        return "#cc00ee";
      case magnitude > 4:
        return "#ea2c2c";
      case magnitude > 3:
        return "#ff833d";
      case magnitude > 2:
        return "#eecc00";
      case magnitude > 1:
        return "#d4ee00";
      default:
        return "#98ee00";
    }
  }
   // Function for the radius of the earthquake marker related to its magnitude.
  
   function getRadius(magnitude) {
    if (magnitude === 0) {
        return 1;
    }
    return magnitude * 4;
    }
  
    // GeoJSON layer with the retrieved data
L.geoJSON(data, {
pointToLayer: function (feature, latlong) {
    return L.circleMarker(latlong);
    },

style: styleInfo,
onEachFeature: function(feature, layer) {
    
  // pop-up with related information 
layer.bindPopup("Earthquake Magnitude: " + feature.properties.mag + "<br>Earthquake Location:<br>" + feature.properties.place);
}
}).addTo(myMap);

//legend 
