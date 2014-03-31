/**
*	FlouCapt ejs_slidein.js
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
if(!document.all && document.getElementById)
         ejs_hauteur = window.innerHeight-400;
 else
         ejs_hauteur = document.body.clientHeight-400;
 
 document.write('<style type="text/css">\n');
 document.write('#ejs_slide_box ');
 document.write('	{');
 document.write('	position:absolute;');
 document.write('	-moz-border-radius: 20px;');
 document.write('	width:280px;');
 document.write('	height:270px;');
 document.write('	left:-300px;');
 document.write('	top:200px;');
 document.write('	background-color:#ffffff;');
 document.write('	border-color:#000000;');
 document.write('	border-width:2px;');
 document.write('	border-style:solid;');
 document.write('	}\n');
 
 document.write('#ejs_slide_image ');
 document.write('	{');
 document.write('	position:relative;');
 document.write('	-moz-border-radius: 20px;');
 document.write('	top:7px;');
 document.write('	left:7px;');
 document.write('	}\n');
 
 document.write('.ejs_slide_blanc\n');
 document.write('	{\n');
 document.write('	color:#ffffff;');
 document.write('	font-family:arial;');
 document.write('	font-weight:bold;');
 document.write('	font-size:15px;');
 document.write('	text-decoration:none;');
 document.write('	}');
 document.write('</style>');
 
 var slide_tempo;
 slide_url_image = 'images/pub.png';
 slide_x = -290;
 slide_ismoving = false;

 
 function slide_start()
 	{
 	if(slide_x == -290 && !slide_ismoving)
 		slide_deballe();
 	else if(!slide_ismoving)
 		slide_remballe();
 	}
 
 function slide_deballe()
 	{
 	slide_ismoving = true;
 	if(slide_x < 0)
 		{
 		slide_x += 5;
 		slide_move();
 		setTimeout("slide_deballe()", 20);
 		}
 	else
 		{
 		slide_ismoving = false;
 		setTimeout("slide_start()",3000);
 		}	
 	}
 
 function slide_remballe()
 	{
 	clearTimeout(slide_tempo);
 	slide_ismoving = true;
 	if(slide_x > -290)
 		{
 		slide_x -= 5;
 		slide_move();
 		setTimeout("slide_remballe()", 10);
 		}
 	else
 		slide_ismoving = false;
 		setTimeout("slide_start()",25000);
 	}
 
 function slide_move()
 	{
 	if(document.getElementById)
 		{
 		document.getElementById("ejs_slide_box").style.left=slide_x+'px';
 		}
 	}
 
 function slide_close()
 	{
 	if(document.getElementById)
 		{
 		document.getElementById("ejs_slide_box").innerHTML = '';
 		document.getElementById("ejs_slide_box").style.top = -100;
 		document.getElementById("ejs_slide_box").style.left = -100;
 		document.getElementById("ejs_slide_box").style.width = 1;
 		document.getElementById("ejs_slide_box").style.height = 1;
 		}
 	}
 
 window.onload = setTimeout("slide_start()",9000);

 

 document.write('<div id="ejs_slide_box">');
 document.write('<div id="ejs_slide_image">');
 document.write('<a href="'+slide_url_click+'" target="_blank"><img src="'+slide_url_image+'" border="0" alt="" /></a>');
 document.write('</div>');
 document.write('<div id="ejs_slide_bouton"><a href="#" onclick="slide_start();this.blur();return(false)" class="ejs_slide_blanc">><br /><</a><br /><a href="#" onclick="slide_close();return(false)" class="ejs_slide_blanc">x</a></div>');
 document.write('</div>');
