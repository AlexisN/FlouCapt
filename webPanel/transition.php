<?php 
$file = fopen('conf/picture.txt', 'r');
$line = fgets($file); 
echo($line);
fclose($file); 
?>
