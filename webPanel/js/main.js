var tmp = "";
function loadData (){ 
    var tmp = "";
    $.ajax({
        url: window.location.pathname + "transition.php",
        async: false,
        success: function(result){
           if(isNaN(result) == true){ 
               var data = result.split('|');
               var p = data[1];
               var c = data[0];
               switchData(p, c);}

               else{
                   manageError(result);
               }},
               error: function(result) {
                   manageError(result.status);
               }
           });
}

function bannerPoster(message){

    var x_res = window.innerWidth;
    $('div#error').stop(true,true).hide().fadeIn();
    $('div#error').text(message);
    $('img#picOne').attr('alt', '');

}

function manageError(status){

   switch(status){

        case 0:
        // Error file config

        bannerPoster('File config');
        break;
        case '1':
        // Error The picture retrieve by the camera is not valid
        bannerPoster('The picture retrieve by the camera is not valid');
        break;
        case '2':
        // Error Unable to contact the camera
        bannerPoster('Unable to contact the camera');
        break;
        case 404:
        // Error la page n'existe pas
        bannerPoster('The transition page can not be contacted');
        break;
        case 500:
        //Error Internal Server Error
        bannerPoster('Erreur Internal Server Error');
        break;
        case 502:
        // Error Bad Gateway ou Proxy Error
        bannerPoster('Bad Gateway ou Proxy Error');
        break;
        case 509:
        // Error Bandwidth Limit Exceeded
        bannerPoster('Bandwidth Limit Exceeded');
        break;
        default:
        //Error default
        bannerPoster('Erreur de type inconnue');
        break;
    }
}


function switchData(pLink, cLink){

    $('div#error').fadeOut();
    var x_res = window.innerWidth;
    var y_res = window.innerHeight;
    document.getElementById('picOne').style.width = x_res - 50 + 'px';
    document.getElementById('picOne').style.height = y_res - 50 + 'px';

    if(tmp == pLink){

    }
    else{
        $("#picOne").fadeOut( 'slow' ).attr('src',pLink).stop(true,true).hide().fadeIn('slow');
        $("a#dwd").attr( 'href', pLink);
        tmp = pLink;}
    }
    //Advertisement
    function ad() {
        $('.pub').fadeIn("slow").delay(10000).fadeOut("slow");
    }


$( document ).ready(function() {
  
    setInterval(loadData,1000);
    var pepe = $.fn.fullpage({
        slidesColor: ['#424242', '#4BBFC3'],
        anchors: ['firstPage', 'secondPage'],
        menu: '#menu',
        easing: 'easeOutBack'});
    $('.pub').hide();
    setInterval(ad, 25000);  
});

