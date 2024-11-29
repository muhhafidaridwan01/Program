<?php
include("../controllers/CalonMahasiswa.php"); // Menyertakan file controller untuk Karyawan
include("../lib/functions.php"); // Menyertakan file library untuk fungsi tambahan
$obj = new CalonMahasiswaController(); // Membuat objek KaryawanController
$rows = $obj->getCalonMahasiswaList(); // Mengambil data daftar karyawan dari controller
?>
<html>
<head>
    <title>Calon Mahasiswa</title> <!-- Judul halaman -->
    <script src="https://cdn.tailwindcss.com"></script> <!-- Menyertakan CDN Tailwind CSS untuk styling -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"> <!-- Menyertakan CDN Font Awesome untuk ikon -->
</head>
<body class="bg-cover bg-center bg-fixed" style="background-image: url('foto_pt.jpg');"> <!-- Menetapkan gambar latar belakang -->
    <div class="bg-gray-100 bg-opacity-50 p-6 min-h-screen"> <!-- Membuat latar belakang transparan dan padding -->
        <div class="max-w-6xl mx-auto bg-white rounded-lg shadow-lg p-6"> <!-- Kotak utama dengan lebar maksimal dan padding -->
            <h1 class="text-3xl font-bold mb-4 text-center">Daftar Calon Mahasiswa</h1> <!-- Judul utama halaman -->
            <p class="text-gray-600 text-center mb-6">List Data Mahasiswa</p> <!-- Keterangan di bawah judul -->

            <!-- Tombol untuk menambah data karyawan -->
            <a class="bg-green-500 text-white px-5 py-2 rounded shadow-md mb-4 inline-block hover:bg-green-600 transition duration-300" href="add.php">
                Tambah Data
            </a>
            
            <!-- Table untuk menampilkan data karyawan -->
            <div class="overflow-x-auto">
                <table class="min-w-full bg-white border border-blue-500 rounded-lg shadow-md">
                    <thead class="bg-blue-200">
                        <!-- Header tabel dengan nama kolom -->
                        <tr>
                            <th class="py-3 px-6 border-b border-blue-500 text-left">ID</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-left">No. Registrasi</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-left">Nama</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-left">JK</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-left">Tanggal Lahir</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-left">Asal Sekolah</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-left w-52">Jurusan</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-left w-52">Lulus Tahun</th>
                            <th class="py-3 px-6 border-b border-blue-500 text-center">Aksi</th> <!-- Kolom aksi (edit/hapus) -->
                        </tr>
                    </thead>
                    <tbody>
                        <?php foreach ($rows as $row) { ?> <!-- Mengiterasi setiap data karyawan yang ada -->
                            <tr class="bg-white hover:bg-gray-100 transition duration-200">
                                <!-- Menampilkan setiap data karyawan dalam baris tabel -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['id_cal_mahasiswa']; ?></td> <!-- Menampilkan ID karyawan -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['nomor_registrasi']; ?></td> <!-- Menampilkan NIK -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['nama_cal_mahasiswa']; ?></td> <!-- Menampilkan Nama karyawan -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['jk']; ?></td> <!-- Menampilkan Jenis Kelamin -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['tanggal_lahir']; ?></td> <!-- Menampilkan Departemen -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['sekolah_asal']; ?></td> <!-- Menampilkan Status karyawan -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['jurusan']; ?></td> <!-- Menampilkan Tanggal Masuk -->
                                <td class="py-3 px-6 border-b border-blue-500"><?php echo $row['lulus_tahun']; ?></td> <!-- Menampilkan Tanggal Masuk -->
                                <td class="py-3 px-6 border-b border-blue-500 text-center">
                                    <div class="flex space-x-6 justify-center">
                                        <!-- Tombol untuk Edit data karyawan -->
                                        <a class="bg-blue-600 text-white px-6 py-2 rounded-md hover:bg-blue-700 transition duration-300" href="edit.php?id_cal_mahasiswa=<?php echo $row['id_cal_mahasiswa']; ?>">
                                            Edit
                                        </a>
                                        <!-- Tombol untuk Hapus data karyawan -->
                                        <a class="bg-red-600 text-white px-6 py-2 rounded-md hover:bg-red-700 transition duration-300" href="delete.php?id_cal_mahasiswa=<?php echo $row['id_cal_mahasiswa']; ?>">
                                            Hapus
                                        </a>
                                    </div>
                                </td>
                            </tr>
                        <?php } ?>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>
