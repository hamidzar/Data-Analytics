// from data.js
var tableData = data;
var tbody = d3.select("tbody");
// YOUR CODE HERE!
var button = d3.select("#filter-btn");
// Select the form
var form = d3.select("#form");
// Create event handlers 
button.on("click", runEnter);
form.on("submit",runEnter);
// Complete the event handler function for the form
function runEnter() {
  // Prevent the page from refreshing
  d3.event.preventDefault();
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");
  var inputElement_city = d3.select("#city");
  var inputElement_state = d3.select("#state");
  // Get the value property of the input element
  var inputValue = inputElement.property("value");
  var inputValue_city = inputElement_city.property("value");
  var inputValue_state = inputElement_state.property("value");
  console.log(inputValue);
  console.log(inputValue_city);
  console.log(inputValue_state);
  console.log(tableData);
  //var filteredData = tableData.filter(info => info.datetime == inputValue);
  ///console.log(filteredData);
  // BONUS: Calculate summary statistics for the age field of the filtered data
  // First, create an array with just the age values
  //var cities = filteredData.map(info => info.city);
  tbody.html("")
  var filterData = tableData.filter(info => info.datetime == inputValue);   
data.forEach((tableData) => {
    if ((inputValue !== "") || (inputValue_city !== " ") || (inputValue_state !== " ")){

        if ((tableData.datetime == inputValue) || (tableData.city == inputValue_city) || (tableData.state == inputValue_state)){
            var row = tbody.append("tr");
            Object.entries(tableData).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
    });
  };
};
});
 

};




 