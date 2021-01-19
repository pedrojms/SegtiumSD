function myMap() {

var mapProp= {
    center:new google.maps.LatLng(-2.186542, -79.877620),
    zoom:20,
};
var mapa=new google.maps.Map(document.getElementById("mapa"),mapProp);
var Marcador = new google.maps.Marker({
        position: new google.maps.LatLng(-2.186542, -79.877620),
        map: mapa
    });
}