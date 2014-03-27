<?php
/**
*	FlouCapt transition.php
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
 $file = fopen('conf/picture.txt', 'r');
 $line = fgets($file); 
 echo($line);
 fclose($file); 
?>
