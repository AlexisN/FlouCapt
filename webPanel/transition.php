<?php 
/**
* transition.php, poster link of current and past picture
*/
$file = fopen('conf/picture.txt', 'r'); // Read data into picture.txt
$line = fgets($file); 
echo($line);
fclose($file); 
?>
