<?php
/**
*	FlouCapt data.php
*	https://github.com/AlexisN/FlouCapt
*
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
/** Read data into webconf file*/
function readData($info){


  $file = file("/etc/floucapt/webConf.ini") or die(writeDefault());
  $retour = "";
  if($info == "mdp"){
    $retour = $file[0];
  }
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

  if($info == "link" || $info == "frequency"){
    $cfg = file("/etc/floucapt/config.ini") or die("Not reading cfg");
    if($info == "link"){
      $r = split('=', $cfg[2]);
      $retour = $r[1];
    }
    else{
      $r = split('=', $cfg[1]);
      $retour = $r[1];
    }

  }
  return $retour;
}
/** Create a default web configuration file if WebConf.ini doesn't exist*/
function writeDefault(){

    $default = fopen("/etc/floucapt/webConf.ini", "w");
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

    header("Location:../index.php");
}
?>
