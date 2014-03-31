<?php include('data.php'); ?>

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
    <script type="text/javascript" src="js/main.js"></script>
    <?php echo 
    '<script type="text/javascript">
    $( document ).ready(function() {
        setInterval(function() { ad('.(int)readData("adV").'); }, '.(int)readData("adI").');
    });
    </script>';?>
</head>

<body>

    <!-- Menu (Camera, About us, Download Picture)-->
    <!-- You can delete this to hide buttons-->
    <ul id="menu">
        <li data-menuanchor="firstPage"><a href="#firstPage"  >Camera</a></li>
        <li data-menuanchor="secondPage"><a href="#secondPage"  >About us</a></li>
    </ul>
    <!-- -->

    <!-- First page (Camera)-->
    <div class="section" id="section0">
        <!--This div is empty but if an error occurs, it allowed us to display a message-->
        <div id ="error" class="classname"></div>
        <!--This script display the ad-->
        <?php echo ('<a href="'.readData("adOneL").'"><img id="adOne" src='.readData("adOne").'alt="Advertisement" onerror="errorPicture(1)" class="pub"/></a>')?>
        <!--This tag will display the picture-->
        <img id="picOne" style="" src="" alt="WAIT..."/>
    </div>

    <!-- Second page (About us)-->
    <!-- You can delete this to hide the second page-->
    <div class="section" id="section1">
        <p><?php echo(readData("about"))?></p>
        <br/>
        <!--this part give more informations about the project or the place which is filmed, you can change the text and the ad on the Admin Panel thanks to this script-->
        <?php echo ('<a href="'.readData("adTwoL").'"><img id="adTwo" src='.readData("adTwo").' alt="Advertisement" onerror="errorPicture(2)"/></a> ')?>
    </div>
    <!-- -->
</div>
</body>
</html>

