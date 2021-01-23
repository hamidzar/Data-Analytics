function megaData(sample){
  d3.json("samples.json").then((data) => {
      var metadata = data.metadata;
      var metadataFiltered = metadata.filter(d =>d.id == sample)[0];
      console.log(metadataFiltered);
      var graphData = d3.select("#sample-metadata");
      // clearing previous data
      graphData.html("");
      graphData.append("h5").text(`id: ${metadataFiltered.id}`);
      graphData.append("h5").text(`ethnicity: ${metadataFiltered.ethnicity}`);
      graphData.append("h5").text(`gender: ${metadataFiltered.gender}`);
      graphData.append("h5").text(`age: ${metadataFiltered.age}`);
      graphData.append("h5").text(`location: ${metadataFiltered.location}`);
      graphData.append("h5").text(`bbtype: ${metadataFiltered.bbtype}`);
      graphData.append("h5").text(`wfreq: ${metadataFiltered.wfreq}`);
      // Object.entries(metadataFiltered).forEach((key) => {graphData.append("h5").text});
  });

};
