
<?php
/**
*	FlouCapt config.php
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
$file = fopen("/etc/floucapt/webConf.ini", 'r');
$mdp =fgets($file);
$longueur_chaine=strlen($mdp);
$_admin_pass = substr($mdp, 0, $longueur_chaine-1);
$_admin_login = 'login';
?>

