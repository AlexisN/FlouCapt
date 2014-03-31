/**
*	FlouCapt main.js
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
var testPastLink = "";
var x_res = window.innerWidth; // Width of curent window
var y_res = window.innerHeight; // Height of curent window
/**
*loadData()
*Use ajax to contact transition.php
*Call manageError() if error is detected
*/
function loadData (){

   $.ajax({
        url: "transition.php",
        async: false,
        success: function(result){
            if(isNaN(result) == true){  // If result isn't a number, it's the link of picture
                var data = result.split('|');
                var p = data[1];
                var c = data[0];
                switchData(p, c);}
                else if((result=="") || (result == null)){ //If result is equal null the picture processing program have no contact picture.txt
                    manageError('null');
                }
                else{ // Call manageError() with error of picture processing program 
                    manageError(result);
                }},
                error: function(result) { //  Call manageError() with result of request if is not possible to contact transition.php
                    manageError(result.status);

                }
            });
}

/**
*bannerPoster(message)
*Displayes the error message
*parameter message: text write
*/
function bannerPoster(message){

    var x_res = window.innerWidth;
    $('div#error').stop(true,true).hide().fadeIn();
    $('div#error').text(message);
    $('img#picOne').attr('alt', '');

}

/**
*manageError(status)
*status: error number
*manage error and call bannerPoster(message)
*/
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
	break;}
}

/**
*switchData(pLink, cLink)
*parameter pLink: the link of past picture
*parameter cLink: the link of current picture
*Allows the transition between the images 
**/
function switchData(pLink, cLink){

    $('div#error').fadeOut(); // Hide error text
    document.getElementById('picOne').style.width = x_res - 50 + 'px'; // Adjust the picture width of the screen
    document.getElementById('picOne').style.height = y_res - 50 + 'px'; // Adjust the picture height of the screen
 
    if(testPastLink != cLink){ // if past link isn't diffenrent of current link the picture does not change
        $("#picOne").fadeOut( 'slow' ).attr('src',cLink).stop(true,true).hide().fadeIn('slow'); //  transition with jQuery
        testPastLink = cLink;  
    }
}

/**
*ad(time)
*parameter time : time in milliseconds of advertisment is displayed
*Manage advertisement displaye
*/
function ad(time) {

    var tAd = $('.pub').innerWidth(); // Width of advertisements
    var rdm = Math.floor(Math.random()*(x_res+1-tAd)); // Random for place of advertisement
    $('.pub').attr('style', 'left:'+rdm+'px'); // change left attribute
    $('.pub').fadeIn("slow").delay(time).fadeOut("slow"); //transition
}

$( document ).ready(function() {
    setInterval(loadData,5000); // Call loadData() all five seconds
    var pepe = $.fn.fullpage({
        slidesColor: ['#000000', '#4BBFC3'], // Color of first and second screen
        anchors: ['firstPage', 'secondPage'],
        menu: '#menu', //button
        easing: 'easeOutBack'});
    $('.pub').hide();
});

