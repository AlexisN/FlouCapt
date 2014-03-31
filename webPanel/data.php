<?php

function readData($info){

    $file = file("/etc/floucapt/webConf.ini") or die(writeDefault());

    $retour = "";
    if($info == "name"){
        $retour = $file[1];
    }
    elseif($info == "adOne"){
        $retour = $file[2];
    }
    elseif($info == "adOneL"){
        $retour = $file[3];
    }
    elseif($info == "adTwo"){
        $retour = $file[4];
    }
    elseif($info == "adTwoL"){
        $retour = $file[5];
    }
    elseif($info == "adV"){
        $retour = $file[6];
    }
    elseif($info == "adI"){
        $retour = $file[7];
    }
    elseif($info == "about"){
        for( $i = 8; $i < count($file); $i++ ){
            $retour .= $file[$i];
        }
    }
    return $retour;
}

function writeDefault(){

    $default = fopen("/etc/floucapt/webConf.ini", "w");// Chemin vers webConf !!!
    fwrite($default, "default"."\n");
    fwrite($default, "default"."\n");
    fwrite($default, "images/def.jpg"."\n");
    fwrite($default, "images/def.jpg"."\n");
    fwrite($default, "images/def.jpg"."\n");
    fwrite($default, "images/def.jpg"."\n");
    fwrite($default, "30000"."\n");
    fwrite($default, "30000"."\n");
    fwrite($default, "default");
    fclose($default);
    header("Location:index.php");

}
?>

