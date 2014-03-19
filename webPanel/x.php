<?php 
 $file = fopen('picture.txt', 'r'); 
 $line = fgets($file); 
 echo($line);
 fclose($file); 
?>