<?php

$pis = array(
        '192.168.1.10',
        '192.168.1.11',
        '192.168.1.12'
);

$data = '<html><head><meta http-equiv="refresh" content="3"></head><body>';

for ($i = 0; $i < count($pis); $i++) {
	$sock = @fsockopen($pis[$i], 22, $errno, $errstr, 1);
	if ($sock) {
		$data .= '<p>pi'.$i.': ON</p>';
	} else {
		$data .= '<p>pi'.$i.': OFF</p>';
	}
	fclose($sock);
}

try {
	$db = new PDO('sqlite:/home/pi/raspi-rfid-tracking/src/measurements.db');
	
	$data .= '<table border=1>';
	$data .= '<tr><td>num</td><td>tag_id</td><td>rss</td></tr>';
	$result = $db->query('SELECT * FROM rfid ORDER BY num DESC');
	foreach($result as $row) {
		$data .= '<tr><td>'.$row['num'].'</td>';
		$data .= '<td>'.$row['tag_id'].'</td>';
		$data .= '<td>'.$row['rss'].'</td></tr>';
	}
	$data .= '</table>';
	$db = NULL;
} catch(PDOException $e) {
	print 'Exception: '.$e->getMessage();
}

$data .= '</body></html>';

echo $data;

?>
