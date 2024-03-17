<?php 
header('Content-Type: application/json');
include_once('Kartun.php');

$fun = new Kartun();

$json = array();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

	$jsonData = file_get_contents('php://input');

	$data = json_decode($jsonData, true);

	if ($data !== null) {

		$text = array('sms'=> $fun->sizeUpdate($data));

		array_push($json,$text);

	}
}

echo json_encode($json);

?>