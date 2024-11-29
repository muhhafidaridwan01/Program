<?php
// Menyertakan file model CalonMahasiswaModel.php yang berisi fungsi-fungsi untuk mengelola data calon mahasiswa.
include_once('../models/CalonMahasiswaModel.php');

// Mendefinisikan kelas CalonMahasiswaController
class CalonMahasiswaController
{
    // Mendeklarasikan properti untuk objek model
    private $model;

    // Konstruktor yang akan membuat objek model ketika controller ini dipanggil
    public function __construct()
    {
        // Membuat objek model CalonMahasiswaModel untuk digunakan dalam fungsi-fungsi controller
        $this->model = new CalonMahasiswaModel();
    }

    // Fungsi untuk menambahkan CalonMahasiswa baru ke dalam database
    public function addCalonMahasiswa($nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun)
    {
        // Memanggil fungsi addCalonMahasiswa() dari model untuk menambahkan data calon mahasiswa ke dalam database
        return $this->model->addCalonMahasiswa($nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun);
    }

    // Fungsi untuk mengambil data CalonMahasiswa berdasarkan ID CalonMahasiswa
    public function getCalonMahasiswa($id_cal_mahasiswa)
    {
        // Memanggil fungsi getCalonMahasiswa() dari model untuk mengambil data calon mahasiswa berdasarkan ID
        return $this->model->getCalonMahasiswa($id_cal_mahasiswa);
    }

    // Fungsi untuk memperbarui data calon mahasiswa di database berdasarkan ID calon mahasiswa
    public function updateCalonMahasiswa($id_cal_mahasiswa, $nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun)
    {
        // Pastikan parameter valid
        if (empty($nomor_registrasi) || empty($nama_cal_mahasiswa)) {
            return false; // Tambahkan validasi sesuai kebutuhan
        }
        
        // Memanggil fungsi updateCalonMahasiswa() dari model untuk memperbarui data calon mahasiswa
        return $this->model->updateCalonMahasiswa($id_cal_mahasiswa, $nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun);
    }

    // Fungsi untuk menghapus data CalonMahasiswa berdasarkan ID CalonMahasiswa
    public function deleteCalonMahasiswa($id_cal_mahasiswa)
    {
        // Memanggil fungsi deleteCalonMahasiswa() dari model untuk menghapus data calon mahasiswa dari database
        return $this->model->deleteCalonMahasiswa($id_cal_mahasiswa);
    }

    // Fungsi untuk mengambil daftar seluruh calon mahasiswa
    public function getCalonMahasiswaList()
    {
        // Memanggil fungsi getCalonMahasiswaList() dari model untuk mengambil semua data CalonMahasiswa
        return $this->model->getCalonMahasiswaList();
    }

    // Fungsi untuk mengambil data kombinasi untuk keperluan form (seperti pilihan dropdown)
    public function getDataCombo()
    {
        // Memanggil fungsi getDataCombo() dari model untuk mengambil data kombinasi
        return $this->model->getDataCombo();
    }
}
?>
