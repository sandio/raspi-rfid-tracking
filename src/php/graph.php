<?php

header('content-type: image/png');

$x = 800;
$y = 800;
$l = 40;

$image = imagecreate($x, $y);
$background = imagecolorallocate($image, 255, 255, 255);
$line_color = imagecolorallocate($image, 125, 125, 125);
$point0 = imagecolorallocate($image, 255, 0, 0);
$point1 = imagecolorallocate($image, 0, 255, 0);
$point2 = imagecolorallocate($image, 0, 0, 255);
$point3 = imagecolorallocate($image, 0, 0, 0);
$point4 = imagecolorallocate($image, 125, 125, 125);
$point5 = imagecolorallocate($image, 0, 255, 255);

$colors = [$point0, $point1, $point2];
$colors2 = [$point3, $point4, $point5];

imageline($image, 0, 0, $x, 0,  $line_color);
imageline($image, 0, 0, 0, $y, $line_color);
imageline($image, 0, $y/2, $x, $y/2, $line_color);
imageline($image, $x/2, 0, $x/2, $y, $line_color);

for ($i = $l; $i < $x; $i += $l) {
	imagedashedline($image, $i, 0, $i, $y, $line_color); 
}

for ($i = $l; $i < $y; $i += $l) {
	imagedashedline($image, 0, $i, $x, $i, $line_color); 
}

try {
	$dbh = new PDO('sqlite:/home/pi/raspi-rfid-tracking/src/measurements.db');
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);	
	
	$result = $dbh->query('SELECT x, y, r FROM positions GROUP BY node_name LIMIT 3');
	$index = 0;
	foreach($result as $row) {
		$pos_x = $row['x']*$l + $x/2;
		$pos_y = $row['y']*$l + $y/2;
		$pos_r = $row['r']*2*$l;
		imagefilledellipse($image, $pos_x, $pos_y, 10, 10, $colors[$index]);
		imagearc($image, $pos_x, $pos_y, $pos_r, $pos_r, 0, 360, $colors[$index]);
		$index++;
	}

	$result = $dbh->query('SELECT x, y, z, r FROM positions WHERE node_name=3 OR node_name=4');
	$index = 0;
	foreach($result as $row) {
		$pos_x = $row['x']*$l + $x/2;
		$pos_y = $row['y']*$l + $y/2;
		if ($index == 0) {
			$x1 = $row['x'];
			$y1 = $row['y'];
		} else {
			$x2 = $row['x'];
			$y2 = $row['y'];
		}
		imagefilledellipse($image, $pos_x, $pos_y, 10, 10, $colors2[$index]);
		$index++;
	}
	
	$errx = ($x1 + $x2)/2;
	$erry = ($y1 + $y2)/2;
	$pos_x = $errx*$l + $x/2;
	$pos_y = $erry*$l + $y/2;
	imagefilledellipse($image, $pos_x, $pos_y, 10, 10, $colors2[$index++]);
	
	$dbh = NULL;
} catch(PDOException $e) {
	echo 'Exception: '.$e->getMessage();
}
imagepng($image);
imagedestroy($image);

?>
