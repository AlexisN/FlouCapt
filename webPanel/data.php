<?php
/**
*readData()
*read Data into webConf.ini
*parameter info
*/
function readData($info){

    $file = file("/etc/floucapt/webConf.ini") or die(writeDefault()); // Read data into webConf.ini or call writeDefault()

    $retour = "";
    if($info == "name"){ // Tab name
        $retour = $file[1];
    }
    elseif($info == "adOne"){ // Link of the first picture advertisement
        $retour = $file[2];
    }
    elseif($info == "adOneL"){ // Link  first advertisement
        $retour = $file[3];
    }
    elseif($info == "adTwo"){ // Link of the second picture advertisement
        $retour = $file[4];
    }
    elseif($info == "adTwoL"){ // Link  second advertisement
        $retour = $file[5];
    }
    elseif($info == "adV"){ // number in millisecond for advertisement visible
        $retour = $file[6];
    }
    elseif($info == "adI"){ // number in millisecond for repeat visible
        $retour = $file[7]; 
    }
    elseif($info == "about"){ // About Text
        for( $i = 8; $i < count($file); $i++ ){ // Read all end data
            $retour .= $file[$i];
        }
    }
    return $retour; //return information
}
/**
*writeDefault()
*write default Data into webConf.ini
*if webConf isn't existing
*/
function writeDefault(){

    $default = fopen("/etc/floucapt/webConf.ini", "w+"); //Write default data into Webconf.ini 
    fwrite($default, "admin"."\n"); // Admin Password
    fwrite($default, "default"."\n");// Tab name 
    fwrite($default, "images/def.jpg"."\n");// Link of the first picture advertisement
    fwrite($default, "images/def.jpg"."\n");// Link  first advertisement
    fwrite($default, "images/def.jpg"."\n");// Link of the second picture advertisement
    fwrite($default, "images/def.jpg"."\n");// Link  second advertisement
    fwrite($default, "5000"."\n");// number in millisecond for advertisement visible
    fwrite($default, "10000"."\n");// number in millisecond for repeat visible
    fwrite($default, "default");// About Text
    fclose($default);
    header("Location:index.php");//Redirection for actualisation

}
?>

