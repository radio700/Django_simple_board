setTimeout(initMap,2000)

function initMap() {
  let glat =  document.querySelector("#weather span.lat7");
  let glon =  document.querySelector("#weather span.lon8");
  // console.log(typeof(parseFloat(glat.innerText)));
  // console.log(parseFloat(glat.innerText)); 
  // console.log(parseFloat(glon.innerText));
  const myLatLng = {
    // lat: 35.19011951,
    // lng: 128.127058

    lat: parseFloat(glat.innerText),
    lng: parseFloat(glon.innerText)
  }
  const map = new google.maps.Map(document.getElementById('map'), {
    center: myLatLng,
    scrollwheel: false,
    zoom: 18
  })
  const marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'GitHub'
  })
}

// navigator.geolocation.getCurrentPosition(wgeo, onGeoError);