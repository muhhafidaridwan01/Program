<?php
include_once('../db/database.php');
$db = new Database();

$sql = "SELECT * FROM mahasiswa";
$result = $db->query($sql)->fetchAll(PDO::FETCH_ASSOC);

header('Content-Type: application/json');
echo json_encode($result);
?>