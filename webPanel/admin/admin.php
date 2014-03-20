<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title></title>
    <link href="css/style.css" media="screen" rel="stylesheet" type="text/css"/>
    <link href="css/uniform.css" media="screen" rel="stylesheet" type="text/css"/>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"></script>
    <script type="text/javascript" src="js/jquery.tools.js"></script>
    <script type="text/javascript" src="js/jquery.uniform.min.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
</head>
<body>

<div class="TTWForm-container">
     
     
     <div id="form-title" class="form-title field">
          <h2>
               Admin panel
          </h2>
     </div>
     
     
     <form action="process_form.php" class="TTWForm" method="post" novalidate="">
          
          
          <div id="field2-container" class="field f_100">
               <label for="field2">
                    Name of website
               </label>
               <input name="field2" id="field2" required="required" type="text">
          </div>
          
          
          <div id="field3-container" class="field f_100">
               <label for="field3">
                    Link of ip camera
               </label>
               <input name="field3" id="field3" required="required" type="text">
          </div>
          
          
          <div id="field4-container" class="field f_100">
               <label for="field4">
                    Frequency picture
               </label>
               <input max="6000" min="0" name="field4" id="field4" required="required"
               type="number">
          </div>
          
          
          <div id="form-submit" class="field f_100 clearfix submit">
               <input value="Configure" type="submit">
          </div>
     </form>
</div>

</body>
</html>
