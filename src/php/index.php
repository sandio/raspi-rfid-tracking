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
	
	$result = $dbh->query('SELECT x, y, r FROM positions GROUP BY node_name');
	$c = 0;
	foreach($result as $row) {
		$data .= 'Pi'.$c.': x<input type="text" size=5 
			name="x'.$c.'" value="'.$row['x'].'">
			y<input type="text" size=5
			name="y'.$c.'" value="'.$row['y'].'">
			<b>d = '.$row['r'].'</b> ';
			$x = $row['x'];
			$y = $row['y'];
		$c ++;
	}
	$data .= '<input type="submit"></form><hr>';
	$errx = abs(0 - $x);
	$erry = abs(0 - $y);
	$data .= '<p>'.$errx.' | '.$erry.'</p>';
	$dbh = NULL;
} catch(PDOException $e) {
	echo 'Exception: '.$e->getMessage();
}

$data .= '<img src="graph.php" alt="Graph"><hr>';

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
