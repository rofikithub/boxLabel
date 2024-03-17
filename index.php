<?php
header('Content-Type: application/json');
include_once('Kartun.php');

$fun = new Kartun();

$json = array();

$list = $fun->getAll();



if (isset($list)) {
  while($row = $list->fetch_assoc()) {
    array_push($json, $row);
  }

  echo json_encode($json);
}


?> 