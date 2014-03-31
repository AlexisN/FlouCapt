
<?php
/**
*	FlouCapt identification.php
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
session_start(); // initialise session

include("config.php");


if($_POST && !empty($_POST['login']) && !empty($_POST['mdp']))
{
    $password = $_POST['mdp'];

    if(($_admin_login == $_POST['login']) && ($password == $_admin_pass))
    {
        $_SESSION['_login'] = $_admin_login;
        $_SESSION['_pass'] = $password;

        echo '<p style="color:green">Connexion reussi! </p>';
        header('Location: admin.php');      ;
    }
    else
    {
        echo '<p style="color:red">Mauvais login ou mot de passe</p>';
        include("index.php");
        exit();
    }
}
else{
    echo '<p style="color:red">Login Or Password Empty</p>';
    include("index.php");
    exit();
}
?>

