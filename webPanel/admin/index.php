<?php
if (isset($_POST['pass']) AND $_POST['pass'] == "James1234" AND isset($_POST['pseudo']) AND $_POST['pseudo'] == "James1234")   
{
  header('Location: admin.php');      
}
else
    {
     
?>
            <form method="post" action="index.php">
             
                <p>
                    <label for="pseudo">Login:</label><br/>
                    <input type="text" name="pseudo" id="pseudo" />
                    <br />
                    <label for="pass">Votre mot de passe :</label><br/>
                    <input type="password" name="pass" id="pass" /><br/>
                    <input type="submit" value="Connexion" name="connexion" />
               </p>
            </form>
<?php
 
    }
?>
