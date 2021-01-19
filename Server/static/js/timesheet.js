
function addServicio(div,dia,mes,contenido){
    var div1 = $("<div/>", {
      "class":"timeline__box",
    })
    var div2 = $("<div/>", {
      "class":"timeline__date",
    })
    var div3 = $("<div/>", {
      "class":"timeline__post",
    })
    var div4 = $("<div/>", {
      "class":"timeline__content",
    })
    var span1 = $("<span/>", {
      "class":"timeline__day",
      html: dia
    })
    var span2 = $("<span/>", {
      "class":"timeline__month",
      html: mes
    })
    var p = $("<p/>",{
      html: contenido
    })
    span1.appendTo(div2);
    span2.appendTo(div2);
    div2.appendTo(div1);
    p.appendTo(div4);
    div4.appendTo(div3);
    div3.appendTo(div1);
    div1.appendTo(div);
}

function loadTlXml() {
  $.ajax({
      type: "GET",
      url: "data/LineaTiempo.xml",
      dataType: "xml",
      success: function(xml){
          $(xml).find('item').each(function(){
            var id= $(this).attr('id')
            var div = $("<div/>", {
              "class":"timeline__group",
            })
            var span = $("<span/>", {
              "class":"timeline__year",
              html: id
            })
            span.appendTo(div);
            div.appendTo("#timeline");
            $(this).find('ingreso').each(function(){
              var mes = $(this).find('mes').text();
              var dia = $(this).find('dia').text();
              var contenido = $(this).find('descripcion').text();
              addServicio(div,dia,mes,contenido);
            });
          });
      },
      error: function() {
        alert("Error al procesar el xml");
      }
  });
}

$(document).ready(function(){
  loadTlXml()
});