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

	<div class="TTWForm-container">
		<div id="form-title" class="form-title field">
			<h2>
				FlouCapt Panel
			</h2>

		</div>

		<h3>Please, fill all the form before confirm</h3>

		<form action="process_form.php" class="TTWForm" method="post" novalidate="">

			<table>

				<div id="field1-container" class="field f_100">
					<tr>
						<td>
							<label for="field1">
							Link of the IP Camera
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="link" id="field1" required="required" type="text" value="'.readData("link").'">')?>
						</td>

						<td>
							<img id="L" src="images/help.gif" onMouseOver="divHelp(0)"></img>
						</td>
					</tr>
				</div>


				<div id="field2-container" class="field f_100">
					<tr>
						<td>
							<label for="field2">
								Frequency Picture
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="frequency" id="field2" required="required" type="text" value="'.readData("frequency").'">')?>
						</td>
						<td>
							<img id="F" src="images/help.gif" onMouseOver="divHelp(1)"></img>
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
							<img id="N" src="images/help.gif" onMouseOver="divHelp(2)"></img>
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
							<img id="A" src="images/help.gif" onMouseOver="divHelp(3)"></img>
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
							<img id="lA" src="images/help.gif" onMouseOver="divHelp(4)"></img>
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
							<img id="aTwo" src="images/help.gif" onMouseOver="divHelp(5)"></img>
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
							<img id="lATwo" src="images/help.gif" onMouseOver="divHelp(6)"></img>
						</td>
					</tr>
				</div>

				<div id="field6-container" class="field f_100">
					<tr>
						<td>
							<label for="field6">
								Advertisement time visible
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="adV" id="field6" required="required" type="number" value="'.readData("adV").'">')?>
						</td>
						<td>
							<img id="tV" src="images/help.gif" onMouseOver="divHelp(7)"></img>
						</td>
					</tr>
				</div>

				<div id="field7-container" class="field f_100">
					<tr>
						<td>
							<label for="field7">
								Advertisement Frequency
							</label>
						</td>

						<td class="td1">
							<?php echo('<input name="adI" id="field7" required="required" type="number" value="'.readData("adI").'">')?>
						</td>
						<td>
							<img id="tI" src="images/help.gif" onMouseOver="divHelp(8)"></img>
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
							<img id="tI" src="images/help.gif" onMouseOver="divHelp(10)"></img>
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
							<img id="about" src="images/help.gif" onMouseOver="divHelp(9)"></img>
						</td>
					</tr>
				</table>
				<?php echo('<textarea rows="3" cols="100" name="about" id="field6" required="required">'.readData("about").'</textarea>')?>
				</div>

			</br>
			<div id="form-submit" class="field f_100 clearfix submit">
				<input value="Confirm" type="submit" class="confirm"></input>
			</div>
		</form>
	</div>
					<div id="boxHelp" align="right"></div>

</body>
</html>
