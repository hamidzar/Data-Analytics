function megaData(sample){
  d3.json("samples.json").then((data) => {
      var metadata = data.metadata;
      var filteredData = metadata.filter(d =>d.id == sample)[0];
      console.log(filteredData);
      var demoInfo = d3.select("#sample-metadata");
      // clearing previous data
      demoInfo.html("");
      