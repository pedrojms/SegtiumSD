$(document).ready(function(){
  
  $("button").click(function(e){
    e.preventDefault();

    var texto = $('input#buscador').val();
    
    if(texto.length != 0) {
      

      $('#news .titulo-news').filter(function(index){
        
        $(this).show();
        
        var noticia = $(this).text()
        if(noticia.indexOf(texto) == -1) {
          $(this).hide()
        }

      });

    } else {
      $('#noticias .titulo-news').each(function(){
        $(this).show();
      });
    }

    
    
  })
});