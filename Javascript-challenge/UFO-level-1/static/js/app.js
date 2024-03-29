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
 
  // Get the value property of the input element
  var inputValue = inputElement.property("value");
 
  //Refreshing the page for the new filter / query 
  tbody.html("")

// Generate output based on the date
data.forEach((tableData) => {
   
        if ((tableData.datetime == inputValue)){
            var row = tbody.append("tr");
            Object.entries(tableData).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
    });
  };

});
 

};




 