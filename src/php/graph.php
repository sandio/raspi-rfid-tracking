<?php

header('content-type: image/png');

$x = 800;
$y = 400;
$l = 20;

$image = imagecreate($x, $y);
$background = imagecolorallocate($image, 255, 255, 255);
$line_color = imagecolorallocate($image, 125, 125, 125);
$point_color = imagecolorallocate($image, 255, 0, 0);

imageline($image, 0, 0, $x, 0,  $line_color);
imageline($image, 0, 0, 0, $y, $line_color);

for ($i = $l; $i < $x; $i += $l) {
	imagedashedline($image, $i, 0, $i, $y, $line_color); 
}

for ($i = $l; $i < $y; $i += $l) {
	imagedashedline($image, 0, $i, $x, $i, $line_color); 
}

try {
	$dbh = new PDO('sqlite:/home/pi/raspi-rfid-tracking/src/measurements.db');
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);	
	
	$result = $dbh->query('SELECT x, y, r FROM positions GROUP BY node_name');
	foreach($result as $row) {
		$pos_x = $row['x']*200;
		$pos_y = $row['y']*200;
		$pos_r = $row['r']*2000;
		imagefilledellipse($image, $pos_x, $pos_y, 10, 10, $point_color);
		imagearc($image, $pos_x, $pos_y, $pos_r, $pos_r, 0, 360, $point_color);
	}
	$dbh = NULL;
} catch(PDOException $e) {
	echo 'Exception: '.$e->getMessage();
}
imagepng($image);
imagedestroy($image);

?>
