<?php
header('Content-Type: application/json');
$jsonData = file_get_contents('php://input');
$data = json_decode($jsonData, true);
include_once('Kartun.php');
$fun = new Kartun();





$json = array();


$list = $fun->getSizename();

if (isset($list)) {
  $bno  = 0;
  $tqun = 0;
  while ($rows = $list->fetch_assoc()) {
    $size     = $rows['size'];
    $sizename = $fun->getSize($size);
    $quntaty  = $fun->getQun($size);
    $tpice    = $fun->totalPice();
    $row      = $fun->getFirst($size);

    $qty = 10;
    $ext = 0;
    $no  = 0;
    for ($x = $qty;$x <= $quntaty; $x+=$qty) {
      $bno++;
      $no++;
      $box = array(
        'bestellnr'  => $row['bestellnr'],
        'artsnr'     => $row['artsnr'],
        'artikelbez' => $row['artikelbez'],
        'soko'       => $row['soko'],
        'plinie'     => $row['plinie'],
        'farbe'      => $row['farbe'],
        'saison'     => $row['saison'],
        'kollektion' => $row['kollektion'],
        'eancode'    => $row['eancode'],
        'size'       => $row['size'],
        'qofPieces'  => $qty,
        'sMarking'   => $row['sMarking'],
        'sShort'     => $row['sShort'],
        'grossWt'    => $row['grossWt'],
        'netWt'      => $row['netWt'],
        'cartonNo'   => $bno
      );
      array_push($json,$box);
    }

    $ext = $quntaty-($no*$qty);
    if($ext>0){
      $bno = $bno+1;
      $ebox = array(
        'bestellnr'  => $row['bestellnr'],
        'artsnr'     => $row['artsnr'],
        'artikelbez' => $row['artikelbez'],
        'soko'       => $row['soko'],
        'plinie'     => $row['plinie'],
        'farbe'      => $row['farbe'],
        'saison'     => $row['saison'],
        'kollektion' => $row['kollektion'],
        'eancode'    => $row['eancode'],
        'size'       => $row['size'],
        'qofPieces'  => $ext,
        'sMarking'   => $row['sMarking'],
        'sShort'     => $row['sShort'],
        'grossWt'    => $row['grossWt'],
        'netWt'      => $row['netWt'],
        'cartonNo'   => $bno

      );
      array_push($json,$ebox);
    }
    $tqun += $quntaty;
  }
}

echo json_encode($json);
// echo $fun->getQun("L");
//echo $fun->totalPice();
//echo $tqun;


?> 