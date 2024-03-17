<?php
$path = realpath(dirname(__FILE__));
	include_once($path . "/Database.php");
?>

<?php 

class Kartun
{
	private $db;

	public function __construct()
	{
		$this->db = new Database();
	}


	function getAll()
	{
	    $query  = "SELECT * FROM tbl_xml ORDER BY xml";
	    $result = $this->db->select($query);
	    if ($result != false) {
			return $result;
	    }
	}

	function totalPice()
	{
	    $query  = "SELECT SUM(qofPieces) FROM tbl_xml";
	    $result = $this->db->select($query);
	    if ($result != false) {
			$row = $result->fetch_assoc();
			return $row['SUM(qofPieces)'];
	    }
	}

	function getSizename()
	{
	    $query  = "SELECT DISTINCT size FROM tbl_xml ORDER BY xml";
	    $result = $this->db->select($query);
	    if ($result != false) {
	        return $result;
	    }
	}

	function getFirst($size)
	{
	    $query  = "SELECT * FROM tbl_xml WHERE size='$size' LIMIT 1";
	    $result = $this->db->select($query);
	    if ($result != false) {
	        return $result->fetch_assoc();
	    }
	}

	function getSize($size)
	{
	    $query  = "SELECT * FROM tbl_xml WHERE size='$size'";
	    $result = $this->db->select($query);
	    if ($result != false) {
	        return $result->num_rows;
	    }
	}

	function getQun($size)
	{
	    $query  = "SELECT SUM(qofPieces) FROM tbl_xml WHERE size='$size'";
	    $result = $this->db->select($query);
	    if ($result != false) {
			$row = $result->fetch_assoc();
			return $row['SUM(qofPieces)'];
	    }
	}

	function delete()
	{
	    $query  = "DELETE FROM tbl_xml";
	    $result = $this->db->delete($query);
	    if ($result != false) {
			return "Delete success";
	    }
	}

	function save($data)
	{
	   $xml        = mysqli_real_escape_string($this->db->link,$data['xml']);
	   $bestellnr  = mysqli_real_escape_string($this->db->link,$data['bestellnr']);
	   $artsnr     = mysqli_real_escape_string($this->db->link,$data['artsnr']);
	   $artikelbez = mysqli_real_escape_string($this->db->link,$data['artikelbez']);
	   $soko       = mysqli_real_escape_string($this->db->link,$data['soko']);
	   $plinie     = mysqli_real_escape_string($this->db->link,$data['plinie']);
	   $farbe      = mysqli_real_escape_string($this->db->link,$data['farbe']);
	   $saison     = mysqli_real_escape_string($this->db->link,$data['saison']);
	   $kollektion = mysqli_real_escape_string($this->db->link,$data['kollektion']);
	   $eancode    = mysqli_real_escape_string($this->db->link,$data['eancode']);
	   $size       = mysqli_real_escape_string($this->db->link,$data['size']);
	   $qofPieces  = mysqli_real_escape_string($this->db->link,$data['qofPieces']);
	   $sMarking   = mysqli_real_escape_string($this->db->link,$data['sMarking']);
	   $sShort     = mysqli_real_escape_string($this->db->link,$data['sShort']);
	   $grossWt    = mysqli_real_escape_string($this->db->link,$data['grossWt']);
	   $netWt      = mysqli_real_escape_string($this->db->link,$data['netWt']);
	   $cartonNo   = mysqli_real_escape_string($this->db->link,$data['cartonNo']);


		$query = "INSERT INTO tbl_xml (xml,bestellnr,artsnr,artikelbez,soko,plinie,farbe,saison,kollektion,eancode,size,qofPieces,sMarking,sShort,grossWt,netWt,cartonNo)
		VALUES ('$xml','$bestellnr','$artsnr','$artikelbez','$soko','$plinie','$farbe','$saison','$kollektion','$eancode','$size','$qofPieces','$sMarking','$sShort','$grossWt','$netWt','$cartonNo')";
		$result = $this->db->insert($query);
		if ($result != false) {
		  return "Insert success";
		}

	}


	function sizeUpdate($data)
	{
	   $xml        = mysqli_real_escape_string($this->db->link,$data['xml']);
	   $size       = mysqli_real_escape_string($this->db->link,$data['size']);
	   $bestellnr  = mysqli_real_escape_string($this->db->link,$data['bestellnr']);

		$query = "UPDATE tbl_xml SET size='$size' WHERE bestellnr='$bestellnr' AND xml='$xml'";
		$result = $this->db->update($query);
		if ($result != false) {
		  return "Updated success";
		}
	}









}

?>