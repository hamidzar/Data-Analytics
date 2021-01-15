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
  // Select the input element(s) and get the raw HTML node
  var inputElement = d3.select("#datetime");
  var inputElement_city = d3.select("#city");
  var inputElement_state = d3.select("#state");

  // Get the value property of the input element(s)
  var inputValue_date = inputElement.property("value");
  var inputValue_city = inputElement_city.property("value");
  var inputValue_state = inputElement_state.property("value");
  console.log(inputValue_date);
  console.log(inputValue_city);
  console.log(inputValue_state);
  console.log(tableData);
  
   
  //Refreshing the page for the new filter / query 
  tbody.html("")

// Checking different status for three fileds Date, State and City
// The one(s) that is not empty will be counted for the filter
data.forEach((tableData) => {

  if ((inputValue_date !== "") && (inputValue_state == "") && (inputValue_city == "")){
    if ((tableData.datetime == inputValue_date)){
      // Call the Function that generates the output based on the filter
      populate_table (tableData);
    };
  };


  if ((inputValue_date == "") && (inputValue_state !== "") && (inputValue_city == "")){
    if ((tableData.state == inputValue_state)){
      // Call the Function that generates the output based on the filter
      populate_table (tableData);
    };
  };


  if ((inputValue_date == "") && (inputValue_state == "") && (inputValue_city !== "")){
    if ((tableData.city == inputValue_city)){
      // Call the Function that generates the output based on the filter
      populate_table (tableData);
    };
  };

  if ((inputValue_date !== "") && (inputValue_state !== "") && (inputValue_city == "")){
      if ((tableData.datetime == inputValue_date) && (tableData.state == inputValue_state)){
        // Call the Function that generates the output based on the filter
        populate_table (tableData);
    };
  };

  if ((inputValue_date !== "") && (inputValue_state == "") && (inputValue_city !== "")){
    if ((tableData.datetime == inputValue_date) && (tableData.city == inputValue_city)){
      // Call the Function that generates the output based on the filter
      populate_table (tableData);
    };
  };

  if ((inputValue_date == "") && (inputValue_state !== "") && (inputValue_city !== "")){
    if ((tableData.state == inputValue_state) && (tableData.city == inputValue_city)){
      // Call the Function that generates the output based on the filter
      populate_table (tableData);
    };
  };

  if ((inputValue_date !== "") && (inputValue_state !== "") && (inputValue_city !== "")){
    if ((tableData.datetime == inputValue_date) && (tableData.state == inputValue_state) && (tableData.city == inputValue_city)){
      // Call the Function that generates the output based on the filter
        populate_table (tableData); 
  };
};

});

// Function that generates the output based on the filter
function populate_table (tableData) {
  var row = tbody.append("tr");
  Object.entries(tableData).forEach(([key, value]) => {
  var cell = row.append("td");
  cell.text(value);
  });

}

};




 