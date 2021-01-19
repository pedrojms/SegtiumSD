
/*
function addServicio(titulo, contenido,b1,b2,b3,b4,b1im,b2im,b3im,b4im,imagen){
    var title = $("<h2/>", {
      "class":"card-title",
      html: titulo
    })

    var p = $("<p/>",{
      "class": "card-text",
      html: contenido
    })


    var bene1=$("<p/>",{
      "class": "card-text col-12",
      html: b1
    })

    var bene2=$("<p/>",{
      "class": "card-text col-12",
      html: b2
    })

    var bene3=$("<p/>",{
      "class": "card-text col-12",
      html: b3
    })

    var bene4=$("<p/>",{
      "class": "card-text col-12",
      html: b4
    })

    var img1=$('<img/>',{
      "class": "col-12",
      "src":b1im
    });

    var img2=$('<img/>',{
      "class": "col-12",
      "src":b2im
    });

    var img3=$('<img/>',{
      "class": "col-12",
      "src":b3im
    });

    var img4=$('<img/>',{
      "class": "col-12",
      "src":b4im
    });

    var imagenserv=$('<img/>',{
      "src":imagen
    });
    
    title.appendTo("#txt-ser" );
    imagenserv.appendTo("#imagen-ser");
    p.appendTo("#txt-ser" );
    img1.appendTo("#bene1");
    img2.appendTo("#bene2");
    img3.appendTo("#bene3");
    img4.appendTo("#bene4");
    bene1.appendTo( "#bene1" )
    bene2.appendTo( "#bene2" );
    bene3.appendTo( "#bene3" );
    bene4.appendTo( "#bene4" );

}
*/
function ethBoton(){
  document.getElementById("active").setAttribute('id','inactive')
  document.querySelector('[ href=3]').setAttribute('id','active')

}

function cyberBoton(){
  document.querySelector('[ id="active"]').setAttribute('id','inactive')
  document.querySelector('[ href=1]').setAttribute('id','active')

}

function ISOBoton(){
  document.getElementById("active").setAttribute('id','inactive')
  document.querySelector('[ href=2]').setAttribute('id','active')

}

function codeBoton(){
  document.getElementById("active").setAttribute('id','inactive')
  document.querySelector('[ href=4]').setAttribute('id','active')

}
/*
function loadServiciosXml(seleccionado){
    var pg = require(‘pg’);
    var connectionString = "postgres://djando_windows:1997@PostgreSQL9.4/ip:port/segtiumSA";
    var pgClient = new pg.Client(connectionString);
    pgClient.connect();
    print("connect")
    var query = pgClient.query("SELECT * from servicio where name ="+seleccionado);
    query.on("row", function(row,result){
      result.addRow(row);
    });

    query.on("end", function(result){

    if(result.rows[0] === undefined){

        return;

    }

    else{

    var id = result.rows[0].id;
    var nombre=result.rows[0].nombre;
    var desc=result.rows[0].nombre;
    var ben=result.rows[0].beneficios;

    addServicio(nombre, desc,ben,ben,ben,ben,"https://via.placeholder.com/250x250</","https://via.placeholder.com/250x250</","https://via.placeholder.com/250x250</","https://via.placeholder.com/250x250</","https://via.placeholder.com/300x300</")


    }

    pgClient.end();

  });
}*/

/*

function loadServiciosXml(seleccionado) {
  $.ajax({
      type: "GET",
      url: "data/Servicios.xml",
      dataType: "xml",
      success: function(xml){
          $(xml).find('item').each(function(){
            var id= $(this).attr('servicio')
            if(seleccionado==id){
              var titulo = $(this).find('titulo').text();
              var contenido = $(this).find('descripcion').text();
              var b1=$(this).find('beneficio1').text();
              var b2=$(this).find('beneficio2').text();
              var b3=$(this).find('beneficio3').text();
              var b4=$(this).find('beneficio4').text();
              var b1im=$(this).find('bene1imagen').text();
              var b2im=$(this).find('bene2imagen').text();
              var b3im=$(this).find('bene3imagen').text();
              var b4im=$(this).find('bene4imagen').text();
              var imagen=$(this).find('imagenser').text();
              
              addServicio(titulo, contenido,b1,b2,b3,b4,b1im,b2im,b3im,b4im,imagen)
            }

          });
      },
      error: function() {
        alert("Error al procesar el xml");
      }
  });
}

$(document).ready(function(){

});*/