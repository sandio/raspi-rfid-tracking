<?php

$pis = array(
        '192.168.1.10',
        '192.168.1.11',
        '192.168.1.12'
);

$data = '<html><head><meta http-equiv="refresh" content="3"></head><body>';
#$data = '<html><head></head><body>';


$data .= '<form action="update_pos.php" method="post">';
try {
	$dbh = new PDO('sqlite:/home/pi/raspi-rfid-tracking/src/measurements.db');
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);	
	
	$result = $dbh->query('SELECT x, y, z, r FROM positions GROUP BY node_name');
	$c = 0;
	foreach($result as $row) {
		$data .= 'Pi'.$c.': x<input type="text" size=5 
			name="x'.$c.'" value="'.$row['x'].'">
			y<input type="text" size=5
			name="y'.$c.'" value="'.$row['y'].'">
			z<input type="text" size=5
			name="z'.$c.'" value="'.$row['z'].'">
			<b>d = '.$row['r'].'</b> ';
		$c ++;
	}
	$data .= '<input type="submit"></form><hr>';
	
	$result = $dbh->query('SELECT x, y, z, r FROM positions WHERE node_name=3 OR node_name=4');
	$c =0;
	foreach($result as $row) {
		$data .= '<p>x:'.$row['x'].' y:'.$row['y'].' z:'.$row['z'].'</p>';
		if ($c == 0) {
			$x1 = $row['x'];
			$y1 = $row['y'];
			$z1 = $row['z'];
		} else {
			$x2 = $row['x'];
			$y2 = $row['y'];
			$z2 = $row['z'];
		}
		$c ++;
	}
	
	$errx = abs(3.5 - ($x1 + $x2)/2);
	$erry = abs(5.5 - ($y1 + $y2)/2);
	$errz = abs(1.7 - ($z1 + $z2)/2);
	$data .= '<p>'.$errx.' | '.$erry.' | '.$errz.'</p>';
	$dbh = NULL;
} catch(PDOException $e) {
	echo 'Exception: '.$e->getMessage();
}

$data .= '<img src="graph.php" alt="Graph">';

$data .= '<table><tr><td>';

try {
	$dbh = new PDO('sqlite:/home/pi/raspi-rfid-tracking/src/measurements.db');
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);	
	
	$data .= '<table border=1>';
	$data .= '<tr><td>num</td><td>node_name</td><td>tag_id</td><td>rss</td></tr>';
	$result = $dbh->query('SELECT * FROM rfid GROUP BY node_name');
	foreach($result as $row) {
		$data .= '<tr><td>'.$row['num'].'</td>';
		$data .= '<td>'.$row['node_name'].'</td>';
		$data .= '<td>'.$row['tag_id'].'</td>';
		$data .= '<td>'.$row['rss'].'</td></tr>';
	}
	$data .= '</table>';
	$dbh = NULL;
} catch(PDOException $e) {
	print 'Exception: '.$e->getMessage();
}

$data .= '</td><td><table border=1>';

$data .= '<tr><td>node</td><td>status</td></tr>';
for ($i = 0; $i < count($pis); $i++) {
	$sock = @fsockopen($pis[$i], 22, $errno, $errstr, 1);
	if ($sock) {
		$data .= '<tr><td>pi'.$i.'</td><td>ON</td></tr>';
	} else {
		$data .= '<tr><td>pi'.$i.'</td><td>OFF</td></tr>';
	}
}
$data .= '</table></td></tr></table>';

$data .= '</body></html>';

echo $data;

?>
