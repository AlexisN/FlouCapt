/**
*	FlouCapt main.js
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
var tmp = "";
var x_res = window.innerWidth;
var y_res = window.innerHeight;

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
                else if((result=="") || (result == null)){
                    manageError('null');
                }
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
case 'null':
bannerPoster('No picture loaded');
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
// Error Bad Gateway or Proxy Error
bannerPoster('Bad Gateway or Proxy Error');
break;
case 509:
// Error Bandwidth Limit Exceeded
bannerPoster('Bandwidth Limit Exceeded');
break;
default:
//Error default
bannerPoster('Unknow Error');
break;
}
}


function switchData(pLink, cLink){

    $('div#error').fadeOut();
    document.getElementById('picOne').style.width = x_res - 50 + 'px';
    document.getElementById('picOne').style.height = y_res - 50 + 'px';

    if(tmp != cLink){
        $("#picOne").fadeOut( 'slow' ).attr('src',cLink).stop(true,true).hide().fadeIn('slow');
        $("a#dwd").attr( 'href', cLink);
        tmp = cLink;
    }
}

function errorPicture(atr){

    if(atr == 1) { $('#adOne').attr('src', 'images/def.jpg'); }
    if(atr == 2) { $('#adTwo').attr('src', 'images/def.jpg'); }

}

function ad(time) {

    var tAd = $('.pub').innerWidth();
    var rdm = Math.floor(Math.random()*x_res+1);
    var sync = rdm - tAd;
    if(sync < 0 ){ sync = 0;}
    $('.pub').attr('style', 'left:'+sync+'px');
    $('.pub').fadeIn("slow").delay(time).fadeOut("slow");
}

function bg(){
    var MonTableau = ["#000000", "#FFFFFF", "#A4A4A4", "#D8D8D8", "#E6E6E6"];
    var rmd = Math.floor(Math.random()*5);
    return MonTableau[rmd];
}

$( document ).ready(function() {
    setInterval(loadData,5000);
    var pepe = $.fn.fullpage({
        slidesColor: [bg(), '#4BBFC3'],
        anchors: ['firstPage', 'secondPage'],
        menu: '#menu',
        easing: 'easeOutBack'});
    $('.pub').hide();
});

