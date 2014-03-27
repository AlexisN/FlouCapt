<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>

        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <title><?php echo readData("name"); ?></title>
        
        <!--Import CSS-->
        <link rel="stylesheet" href="css/style.css" />
        
        <!--Import JS-->
        <script src="js/skel.min.js"></script>
        <script src="js/init.js"></script>  
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
        <script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.9.1/jquery-ui.min.js"></script>
        <script type="text/javascript" src="js/jquery.fullPage.js"></script>
        <script type="text/javascript" src="js/examples.js"></script>
        <script type="text/javascript" src="js/main.js"></script>    
    </head>

<body>

<!-- Menu (Camera, About us, Download Picture)-->
    <ul id="menu">
        <li data-menuanchor="firstPage"><a href="#firstPage"  >Camera</a></li>
        <li data-menuanchor="secondPage"><a href="#secondPage"  >About us</a></li>
        <li><a href="" id="dwd">Download Picture !</a></li>
    </ul>

<!-- First page (Camera)-->
    <div class="section " id="section0">
        <!--This div is empty but if an error occurs, it allowed us to display a message-->
        <div id ="error" class="classname"></div>
        <!--This script display the ad-->
        <?php echo ('<a href="'.readData("adOneL").'"><img src='.readData("adOne").'alt="Publicité" class="pub" style="left:40%; bottom:5%; position:absolute; z-index:2"/></a>')?>
        <!--This tag will display the picture-->
        <img id="picOne" style="" src="" alt="WAIT..."/>
    </div>

<!-- Second page (About us)-->
    <div class="section" id="section1">
        <p><?php echo(readData("about"))?></p>
        <br/>
        <!--this part give more informations about the project or the place which is filmed, you can change the text and the ad on the Admin Panel thanks to this script-->
        <?php echo ('<a href="'.readData("adTwoL").'"><img src='.readData("adTwo").'alt="Publicité"/></a>')?>

    </div>
</div>
<?php

function readData($info){

  $file = file("conf/webConf.ini") or die(writeDefault());

    $retour = "";
    if($info == "name"){
        $retour = $file[0];
    }
    elseif($info == "adOne"){
        $retour = $file[1];
    }
    elseif($info == "adOneL"){
        $retour = $file[2];
    }
    elseif($info == "adTwo"){
        $retour = $file[3];
    }
    elseif($info == "adTwoL"){
        $retour = $file[4];
    }
    elseif($info == "about"){
        for( $i = 5; $i < count($file); $i++ ){
            $retour .= $file[$i];
        }
    }
    return $retour;
}

function writeDefault(){

        $default = fopen("conf/webConf.ini", "w");// Chemin vers webConf !!! 
        fwrite($default, "default"."\n");
        fwrite($default, "default"."\n");
        fwrite($default, "default"."\n");
        fwrite($default, "default"."\n");
        fwrite($default, "default"."\n");
        fwrite($default, "default"."\n");
        fclose($default);
    }
?>


</body>
</html>

