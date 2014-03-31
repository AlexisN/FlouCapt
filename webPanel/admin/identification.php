
<?php
/**
*	FlouCapt identification.php
*	https://github.com/AlexisN/FlouCapt
*	
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
session_start(); // initialise session

include("config.php");

/**
*Identification.php make all treatments in the page of the connection to the admin panel
*/
if($_POST && !empty($_POST['login']) && !empty($_POST['mdp']))
{
    $password = $_POST['mdp'];

    if(($_admin_login == $_POST['login']) && ($password == $_admin_pass))
    {
        /* Successful connection */
        $_SESSION['_login'] = $_admin_login;
        $_SESSION['_pass'] = $password;

        echo '<p style="color:green">Successful connection !</p>';
        header('Location: admin.php');      ;
    }
    else
    {
        /*If the login or the password is wrong*/
        echo '<p style="color:red">Bad login or password</p>';
        include("index.php");
        exit();
    }
}
else{
    /*If the login or the password is empty*/
    echo '<p style="color:red">Login Or Password Empty</p>';
    include("index.php");
    exit();
}
?>

