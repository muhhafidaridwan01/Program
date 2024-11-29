<?php
// Menyertakan file database.php yang berisi class Database untuk koneksi ke database
include_once('../db/database.php');

// Membuat objek baru dari kelas Database untuk koneksi ke database
$db = new Database();

// Menyusun query SQL untuk mengambil semua data dari tabel 'calonmahasiswa'
$sql = "select * from calonmahasiswa ";  // Query untuk mengambil semua data dari tabel 'calonmahasiswa'

// Menjalankan query SQL yang telah disusun
$sql = 'SELECT * FROM calonmahasiswa'; // Query untuk mengambil seluruh data dari tabel 'calonmahasiswa'

// Eksekusi query dan mengambil hasilnya dalam bentuk array asosiatif
$result = $db->query($sql)->fetchAll(PDO::FETCH_ASSOC);

// Menetapkan header sebagai JSON agar hasil bisa dikirimkan dalam format JSON
header('Content-type: application/json');

// Mengirimkan hasil query dalam format JSON ke browser atau aplikasi yang memanggilnya
echo json_encode($result);
?>
