<html>
<head>
</head>
<body>
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
   $beroep = $_POST["beroep"];
   $stad = $_POST["stad"];
}

if ($beroep) {
   $arguments .= "-b $beroep ";
}
if ($stad) {
   $arguments .= "-s $stad ";
}

$command = "python makelimerick.py $arguments";
#$command = escapeshellcommand($command);
$output = shell_exec($command);

echo $output;

?>

<p>
<form action="limerick.php" method="post">
Score:
<input type="radio" name="score" value="1">1
<input type="radio" name="score" value="2">2
<input type="radio" name="score" value="3">3
<input type="radio" name="score" value="4">4
<input type="radio" name="score" value="5">5
<input type="radio" name="score" value="6">6
<input type="radio" name="score" value="7">7
<input type="radio" name="score" value="8">8
<input type="radio" name="score" value="9">9
<input type="radio" name="score" value="10">10<br>
Beroep: <input type="text" name="beroep"><br>
Stad: <input type="text" name="stad"><br>

<input type="submit">
</form>
</p>
</body>
</html>
