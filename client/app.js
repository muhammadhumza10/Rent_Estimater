function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getBedroomValue() {
  var uiBedroom = document.getElementsByName("uiBedroom");
  for(var i in uiBedroom) {
    if(uiBedroom[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}



function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url_loc = " http://127.0.0.1:5000/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  var url_city = " http://127.0.0.1:5000/get_city_names";
  $.get(url_loc,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });

  $.get(url_city,function(data, status) {
    console.log("got response for get_location_names request");
    if(data) {
        var city = data.city;
        var uicity = document.getElementById("uicity");
        $('#uicity').empty();
        for(var i in city) {
            var opt = new Option(city[i]);
            $('#uicity').append(opt);
        }
    }
});


}

function onClickedEstimatePrice() {

  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bedroom = getBedroomValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var city = document.getElementById("uicity");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
 // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      area_sqft: parseFloat(sqft.value),
      bedroom: bedroom,
      bathrooms: bathrooms,
      city: city.value,  
      location: location.value
    
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Rupees</h2>";
      console.log(status);
  });
}
window.onload = onPageLoad;