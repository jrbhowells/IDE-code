/**
 * @license
 * Copyright 2019 Google LLC. All Rights Reserved.
 * SPDX-License-Identifier: Apache-2.0
 */

/*
Modified J Howells 25.05.2021
IDE Group 1
Dyson School of Design Engineering
*/

 function initMap() {
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 10,
      center: { lat: 51.5, lng: -0.17 },
    });
  
    directionsRenderer.setMap(map);
  
    const onChangeHandler = function () {
      calculateAndDisplayRoute(directionsService, directionsRenderer);
    };
  
    document.getElementById("start").addEventListener("change", onChangeHandler);
    document.getElementById("end").addEventListener("change", onChangeHandler);
  }
  
  function calculateAndDisplayRoute(directionsService, directionsRenderer) {
    directionsService
      .route({
        origin: {
          query: document.getElementById("start").value,
        },
        destination: {
          query: document.getElementById("end").value,
        },
        travelMode: google.maps.TravelMode.BICYCLING,
        unitSystem: google.maps.UnitSystem.METRIC,
      })
      .then((response) => {
        var ary = [];
        var ary2 = [];
        response.routes[0].legs[0].steps.forEach((element) => {
            ary.push([element.start_location.lat(), element.start_location.lng()])
        });

        response.routes[0].overview_path.forEach((element) => {
            ary2.push([element.lat(), element.lng()]);
        });

        let Directions = [ary,ary2];

        console.log(Directions);

        directionsRenderer.setDirections(response);
      })
      .catch((e) => window.alert("Directions request failed due to " + status));
  }
  
  window.initMap = initMap;
  
  