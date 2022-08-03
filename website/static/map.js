var map = L.map('map').setView([39.63577, -79.81244], 14);
var gl = L.mapboxGL({
  attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
  style: 'https://api.maptiler.com/maps/73455dbc-952b-45a4-9de5-ac4d83ddb128/style.json?key=Y2maXYBGC9a3IVVU8eXz'
}).addTo(map);


function uploadImage(id, date, location, description){
    position = location.split(":")
    var marker = L.marker([position[0], position[1]]).addTo(map);
    marker.bindPopup("<b>" + date + "<br>" + description + "<br>" + "<img src='" + id + "'}}>")
}

function getLocation(){
    if(window.navigator.geolocation){
        window.navigator.geolocation.getCurrentPosition(fillLocation, console.log(), {enableHighAccuracy: true});
    }
}

function fillLocation(position){
    const {latitude, longitude} = position.coords;
    document.getElementById("fillLocation").value = latitude + ":" + longitude;

    var marker = L.marker([latitude, longitude]).addTo(map);
}


