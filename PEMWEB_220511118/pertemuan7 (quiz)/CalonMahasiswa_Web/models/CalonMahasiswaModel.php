<?php
include_once('../db/database.php'); // Menyertakan file database untuk koneksi ke database

// Kelas KaryawanModel bertanggung jawab untuk melakukan operasi CRUD pada tabel 'calonmahasiswa' di database
class CalonMahasiswaModel
{
    private $db; // Properti untuk menyimpan objek koneksi database

    // Konstruktor kelas yang akan membuat objek koneksi ke database
    public function __construct()
    {
        $this->db = new Database(); // Membuat objek Database untuk koneksi ke DB
    }

    // Fungsi untuk menambahkan data calonmahasiswa baru ke database
    public function addCalonMahasiswa($nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun)
    {
        // Query SQL untuk menambahkan data calonmahasiswa baru
        $sql = "INSERT INTO calonmahasiswa (nomor_registrasi, nama_cal_mahasiswa, jk, tanggal_lahir, sekolah_asal, jurusan, lulus_tahun) 
                VALUES (:nomor_registrasi, :nama_cal_mahasiswa, :jk, :tanggal_lahir, :sekolah_asal, :jurusan, :lulus_tahun)";
        
        // Parameter yang akan diganti pada query SQL
        $params = array(
            ":nomor_registrasi" => $nomor_registrasi,
            ":nama_cal_mahasiswa" => $nama_cal_mahasiswa,
            ":jk" => $jk,
            ":tanggal_lahir" => $tanggal_lahir,
            ":sekolah_asal" => $sekolah_asal,
            ":jurusan" => $jurusan,
            ":lulus_tahun" => $lulus_tahun,
        );

        // Eksekusi query dengan parameter yang telah diberikan
        $result = $this->db->executeQuery($sql, $params);
        
        // Mengecek apakah eksekusi berhasil dan mengembalikan hasil dalam format JSON
        if ($result) {
            return json_encode(array("success" => true, "message" => "Insert successful"));
        } else {
            return json_encode(array("success" => false, "message" => "Insert failed"));
        }
    }

    // Fungsi untuk mengambil data calonmahasiswa berdasarkan id_cal_mahasiswa
    public function getCalonMahasiswa($id_cal_mahasiswa)
    {
        // Query SQL untuk mengambil data calonmahasiswa berdasarkan ID
        $sql = "SELECT * FROM calonmahasiswa WHERE id_cal_mahasiswa = :id_cal_mahasiswa";
        
        // Parameter untuk mencari berdasarkan id_cal_mahasiswa
        $params = array(":id_cal_mahasiswa" => $id_cal_mahasiswa);
        
        // Mengembalikan data cal_mahasiswa dalam bentuk array asosiatif
        return $this->db->executeQuery($sql, $params)->fetchAll(PDO::FETCH_ASSOC);
    }

    // Fungsi untuk mengupdate data cal_mahasiswa berdasarkan id_cal_mahasiswa
    public function updateCalonMahasiswa($id_cal_mahasiswa, $nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun)
    {
        // Query SQL untuk memperbarui data cal_mahasiswa
        $sql = "UPDATE calonmahasiswa 
                SET nomor_registrasi = :nomor_registrasi, nama_cal_mahasiswa = :nama_cal_mahasiswa, jk = :jk, 
                    tanggal_lahir = :tanggal_lahir, sekolah_asal = :sekolah_asal, jurusan = :jurusan, lulus_tahun = :lulus_tahun
                WHERE id_cal_mahasiswa = :id_cal_mahasiswa";
        
        // Parameter yang akan digunakan untuk mengupdate data
        $params = array(
            ":nomor_registrasi" => $nomor_registrasi,
            ":nama_cal_mahasiswa" => $nama_cal_mahasiswa,
            ":jk" => $jk,
            ":tanggal_lahir" => $tanggal_lahir,
            ":sekolah_asal" => $sekolah_asal,
            ":jurusan" => $jurusan,
            ":lulus_tahun" => $lulus_tahun,
            ":id_cal_mahasiswa" => $id_cal_mahasiswa
        );

        // Eksekusi query update dan mengembalikan hasil dalam format JSON
        $result = $this->db->executeQuery($sql, $params);
        if ($result) {
            return json_encode(array("success" => true, "message" => "Update successful"));
        } else {
            return json_encode(array("success" => false, "message" => "Update failed"));
        }
    }

    // Fungsi untuk menghapus data calonmahasiswa berdasarkan id_cal_mahasiswa
    public function deleteCalonMahasiswa($id_cal_mahasiswa)
    {
        // Query SQL untuk menghapus data calonmahasiswa berdasarkan ID
        $sql = "DELETE FROM calonmahasiswa WHERE id_cal_mahasiswa = :id_cal_mahasiswa";
        
        // Parameter untuk menghapus data berdasarkan id_cal_mahasiswa
        $params = array(":id_cal_mahasiswa" => $id_cal_mahasiswa);
        
        // Eksekusi query delete dan mengembalikan hasil dalam format JSON
        $result = $this->db->executeQuery($sql, $params);
        if ($result) {
            return json_encode(array("success" => true, "message" => "Delete successful"));
        } else {
            return json_encode(array("success" => false, "message" => "Delete failed"));
        }
    }

    // Fungsi untuk mengambil daftar seluruh CalonMahasiswa
    public function getCalonMahasiswaList()
    {
        // Query SQL untuk mengambil semua data calonmahasiswa
        $sql = 'SELECT * FROM calonmahasiswa';
        
        // Mengembalikan hasil query dalam bentuk array asosiatif
        return $this->db->query($sql)->fetchAll(PDO::FETCH_ASSOC);
    }

    // Fungsi untuk mengambil data calonmahasiswa dan mengirimkannya dalam format JSON
    public function getDataCombo()
    {
        // Query SQL untuk mengambil semua data calonmahasiswa
        $sql = 'SELECT * FROM calonmahasiswa';
        
        // Mengambil hasil query
        $data = $this->db->query($sql)->fetchAll(PDO::FETCH_ASSOC);
        
        // Menetapkan header sebagai JSON dan mengirimkan data sebagai JSON
        header('Content-Type: application/json');
        echo json_encode($data);
    }
}
?>
