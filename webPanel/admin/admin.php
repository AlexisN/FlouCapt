

<!--This document display the admin panel-->


<?php
include('verif.php');
include('data.php');
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Admin</title>
  <link href="css/style.css" media="screen" rel="stylesheet" type="text/css"/>
  <link href="css/uniform.css" media="screen" rel="stylesheet" type="text/css"/>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"></script>
  <script type="text/javascript" src="js/jquery.tools.js"></script> 
  <script type="text/javascript" src="js/jquery.uniform.min.js"></script>
  <script type="text/javascript" src="js/main.js"></script>
</head>

<body>

	<!--This class contains all the admin panel-->
	<div class="TTWForm-container">

		<div id="form-title" class="form-title field">
			<h2>
				FlouCapt Panel
			</h2>

		</div>

		<div id="com"><h3>All forms are required</h3></div>

		<!--The form that contains the field that the admin can modify-->
		<form action="process_form.php" class="TTWForm" method="post" novalidate="">

			<!--This table structures the main part of the admin panel.-->
			<!--3 columns that contain : The label, the field and the helper-->
			<table>

				<div id="field1-container" class="field f_100">
					<tr>
						<td>
							<!--Label-->
							<label for="field1">
							Link of the video stream
							</label>
						</td>

						<td class="td1">
							<!--Field-->
							<?php echo('<input name="link" id="field1" required="required" type="text" value="'.readData("link").'">')?>
						</td>

						<td>
							<!--Helper-->
							<img id="L" src="images/help.gif" onMouseOver="divHelp(0)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>
				</div>


				<div id="field2-container" class="field f_100">
					<tr>
						<td>
							<label for="field2">
								Refresh time to recontact the camera 
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="frequency" id="field2" required="required" type="text" value="'.readData("frequency").'">')?>
						</td>
						<td>
							<img id="F" src="images/help.gif" onMouseOver="divHelp(1)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>
				</div>

				<div id="field3-container" class="field f_100">
					<tr>
						<td>
							<label for="field3">
								Name of the Website
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="onglet" id="field3" required="required" type="text" value="'.readData("name").'">')?>
						</td>
						<td>
							<img id="N" src="images/help.gif" onMouseOver="divHelp(2)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>
				</div>

				<div id="field4-container" class="field f_100">
					<tr>
						<td>
							<label for="field4">
								Advertisement 1
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="ad" id="field4" required="required" type="text" value="'.readData("adOne").'">')?>
						</td>
						<td>
							<img id="A" src="images/help.gif" onMouseOver="divHelp(3)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>

					<tr>
						<td>
							<label for="field4">
								Link advertisement
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="adL" id="field4" required="required" type="text" value="'.readData("adOneL").'">')?>
						</td>
						<td>
							<img id="lA" src="images/help.gif" onMouseOver="divHelp(4)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>
				</div>

				<div id="field5-container" class="field f_100">
					<tr>
						<td>
							<label for="field5">
								Advertisement 2
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="adTwo" id="field5" required="required" type="text" value="'.readData("adTwo").'">')?>
						</td>
						<td>
							<img id="aTwo" src="images/help.gif" onMouseOver="divHelp(5)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>

					<tr>
						<td>
							<label for="field5">
								Link advertisement
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="adTwoL" id="field5" required="required" type="text" value="'.readData("adTwoL").'">')?>
						</td>
							<td>
							<img id="lATwo" src="images/help.gif" onMouseOver="divHelp(6)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>
				</div>

				<div id="field6-container" class="field f_100">
					<tr>
						<td>
							<label for="field6">
								Advertisement display duration time
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="adV" id="field6" required="required" type="text" value="'.readData("adV").'">')?>
						</td>
						<td>
							<img id="tV" src="images/help.gif" onMouseOver="divHelp(7)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>
				</div>

				<div id="field7-container" class="field f_100">
					<tr>
						<td>
							<label for="field7">
								How fast the picture reappear
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="adI" id="field7" required="required" type="text" value="'.readData("adI").'">')?>
						</td>
						<td>
							<img id="tI" src="images/help.gif" onMouseOver="divHelp(8)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>

					</tr>
				</div>
					<div id="field8-container" class="field f_100">
					<tr>
						<td>
							<label for="field8">
								Admin Password
							</label>
						</td>

						<td class="td1">
						<?php echo('<input name="mdp" id="field7" required="required" type="text" value="'.readData("mdp").'">')?>
						</td>
						<td>
							<img id="tI" src="images/help.gif" onMouseOver="divHelp(10)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>

					</tr>
				</div>

				<div id="field8-container" class="field f_100">
					<tr>
						<td>
							</br>
							<label for="field9">
								About US - Please use html
							</label>
						</td>
						<td>
							<img id="about" src="images/help.gif" onMouseOver="divHelp(9)" onMouseOut="$('#boxHelp').fadeOut();"></img>
						</td>
					</tr>
				</table>
				<?php echo('<textarea rows="3" cols="100" name="about" id="field6" required="required">'.readData("about").'</textarea>')?>
				</div>

			<!--Button to confirm the new configuration-->
			</br>
			<div id="form-submit" class="field f_100 clearfix submit">
				<input value="Confirm" type="submit" class="confirm"></input>
			</div>
		</form>
	</div>
					<div id="boxHelp" align="right"></div>

</body>
</html>
