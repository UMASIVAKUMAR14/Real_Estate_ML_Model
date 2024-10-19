function getBedValue() {
    var uiBed = document.getElementsByName("uiBed");
    for(var i in uiBed) {
      if(uiBed[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1;
  }


function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; 
  }

function getBalconyValue() {
    var uiBalcony = document.getElementsByName("uiBalcony");
    for(var i in uiBalcony) {
      if(uiBalcony[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1;
  }
  
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft");
    var bed = getBedValue();
    var bath = getBathValue();
    var balcony = getBalconyValue();
    var location = document.getElementById("uiLocations");
    var area_type = document.getElementById("uiAreaType")
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    //var url = "http://127.0.0.1:5000/predict_house_price"; 
    var url = "/api/predict_house_price";
  
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bed: bed,
        bath: bath,
        balcony: balcony,
        location: location.value,
        area_type: area_type.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
function onPageLoad() {
    console.log( "document loaded" );
    //var url = "http://127.0.0.1:5000/get_location_names"; 
    var url = "/api/get_location_names";
    $.get(url,function(data, status) {
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
  }
  
window.onload = onPageLoad;