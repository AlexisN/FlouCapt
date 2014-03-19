<?php 
 $file = fopen('picture.txt', 'r') or die("can't open file"); 
 $line = fgets($file); 
 echo($line);
 fclose($file); 
?>
