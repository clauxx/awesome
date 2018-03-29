<?php

$ch = curl_init();
$url = 'http://pictaculous.com/api/1.0/';
 
if($argv[1]!='') {
	$fields = array('image'=>file_get_contents($argv[1]));
 
	# Set some default CURL options
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_HEADER, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $fields);
	curl_setopt($ch, CURLOPT_URL, $url);
 
	$result = curl_exec($ch);
	$json = json_decode($result, true);
	$colors = $json['info']['colors'];
	$hex_col = array();


	foreach($colors as $color) {
		$hex_col[] = '#' . $color;
	}

	if(sizeof($hex_col) < 5) {
		array_push($hex_col, $hex_col[0], $hex_col[1], $hex_col[0], $hex_col[1]);
	}

	if(sizeof($hex_col) > 5) {
		$hex_col = array_slice($hex_col, 0, 5);
	}

	array_push($hex_col, $argv[1]);
	
	var_dump($hex_col);

	$fp = fopen('colors.csv', 'w');
	fputcsv($fp, $hex_col);
	fclose($fp);

} else {
	echo 'No image selected. Try to use module.php image.jpg !';
}


?>
