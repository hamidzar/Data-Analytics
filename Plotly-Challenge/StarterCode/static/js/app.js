//getting the Data from samples.json file
function Main(sample){
    d3.json("samples.json").then((data) => {
        //Configuring variables and assigniing the related fileds to the variables
        var metadata = data.metadata;
        var metadataFiltered = metadata.filter(d =>d.id == sample)[0];
        console.log(metadataFiltered);
        var graphData = d3.select("#sample-metadata");
        // clearing previous data
        graphData.html("");
        //Appending the data 
        graphData.append("h5").text(`id: ${metadataFiltered.id}`);
        graphData.append("h5").text(`ethnicity: ${metadataFiltered.ethnicity}`);
        graphData.append("h5").text(`gender: ${metadataFiltered.gender}`);
        graphData.append("h5").text(`age: ${metadataFiltered.age}`);
        graphData.append("h5").text(`location: ${metadataFiltered.location}`);
        graphData.append("h5").text(`bbtype: ${metadataFiltered.bbtype}`);
        graphData.append("h5").text(`wfreq: ${metadataFiltered.wfreq}`);
       
    });
  
  };
  
  