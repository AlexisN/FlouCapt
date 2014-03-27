/**
*	FlouCapt ad management scrypt
*	https://github.com/FlouCapt-GroupC/project
*	
*	@author Thomas PERENNEC
*/

var imgObj;					// the ad we want to animate
var animate;				
var freq;					// timing between two function calls (in ms)
var adVisibility = true;	// visibility of the ad
var width;					// exploitable width for the ad moving zone
var height;					// exploitable height for the ad moving zone


/**
*	Main function of the scrypt, called when the page is loaded
*	Call the initializing and the moving functions
*/
function main(){
	this.init();
	//setInterval('blink();',1000);
	this.autoMove();
}

/**
*	Initializing function, called by the main()
*	Set the imgObj variable with the ad picture and the exploitable moving zone for it
*/
function init(){
	imgObj = document.getElementById('ad'); // retrieving the ad picture
	imgObj.style.position= 'absolute'; 		// initializing the position
	
	// setting the width and height of the moving zone
	width = screen.availWidth - imgObj.width; 
	height = screen.availHeight -imgObj.height*2;
	
	// setting the initial position of the picture
	this.reset();
	
	//setting the fraquency of the autoMove() recalls
	freq = 5;
	
}

/**
*	Moving function, called by the main()
*	Make the picture move automatically around the screen, and its visibility
*/
function autoMove(){
	var leftPos = parseInt(imgObj.style.left);
	var topPos = parseInt(imgObj.style.top);
	
	if((leftPos < width)&&(topPos == 0)){
		imgObj.style.left = parseInt(imgObj.style.left) + 1 + 'px';
		animate = setTimeout(autoMove,freq);
	}
	if((leftPos == width)&&(topPos >= 0)){
		imgObj.style.top = parseInt(imgObj.style.top) + 1 + 'px';
		animate = setTimeout(autoMove,freq);
	}
	//not currently working right
	if((leftPos <= width)&&(topPos >= height)){
		imgObj.style.left = parseInt(imgObj.style.left) - 1 + 'px';
		animate = setTimeout(autoMove,freq);
	}
	
}

function stop(){
	this.clearTimeout(animate);
}

function reset(){
	this.stop();
	imgObj.style.left = '0px';
	imgObj.style.top = '0px';
}

function blink(){
	if(adVisibility == true){
		imgObj.style.visibility = 'hidden';
		adVisibility = false;
	}
	else{
		imgObj.style.visibility = 'visible';
		adVisibility = true;
	}
}	

//the main function is called when the page load
window.onload = main;