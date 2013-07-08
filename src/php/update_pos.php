<?php

header('Location: index.php');

$x0 = $_POST['x0'];
$y0 = $_POST['y0'];

$x1 = $_POST['x1'];
$y1 = $_POST['y1'];

$x2 = $_POST['x2'];
$y2 = $_POST['y2'];

try {
	$dbh = new PDO('sqlite:/home/pi/raspi-rfid-tracking/src/measurements.db');
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);	
	$sth = $dbh->prepare('UPDATE positions SET x = ?, y = ? WHERE node_name = ?');
	
	$sth->execute(array($x0, $y0, 0));
	$sth->execute(array($x1, $y1, 1));
	$sth->execute(array($x2, $y2, 2));
	
	$dbh = NULL;
} catch(PDOException $e) {
	echo 'Exception: '.$e->getMessage();
}

exit();

?>
