
<?php
/**
*	FlouCapt verif.php
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
session_start();

include("config.php");

if(!isset($_SESSION['_login']) || !isset($_SESSION['_pass']))
{
    // if it does not detect sessions, is that this person is not connected
    echo '<p><b style="color:red">espace securise</b><br />Connectez vous pour acceder a cette page</p>';
    include("index.php");
    exit();
}
else
{
    // Test if session is good
    if(($_admin_login != $_SESSION['_login']) || ($_SESSION['_pass'] != $_admin_pass))
    {
        echo '<p><b style="color:red">Votre connexion ne semble pas valide</b></p>';
        include("index.php");
        exit();
    }
}
?>

