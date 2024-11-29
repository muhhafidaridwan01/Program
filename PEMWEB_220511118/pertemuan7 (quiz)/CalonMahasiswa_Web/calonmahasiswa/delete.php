<?php
// Menyertakan file controller untuk calon mahasiswa dan fungsi tambahan
include("../controllers/CalonMahasiswa.php");
include("../lib/functions.php");

$obj = new CalonMahasiswaController(); // Membuat objek CalonMahasiswaController untuk mengakses fungsionalitas

// Mengambil ID Calon Mahasiswa dari parameter URL jika tersedia
$id_cal_mahasiswa = null;
if (isset($_GET["id_cal_mahasiswa"])) {
    $id_cal_mahasiswa = $_GET["id_cal_mahasiswa"];
}

$msg = null; // Inisialisasi pesan sebagai null
// Memproses data POST jika form telah dikirimkan
if (isset($_POST['submitted']) && $_SERVER['REQUEST_METHOD'] == 'POST') {
    // Memastikan ID Calon Mahasiswa diambil dari form POST
    if (isset($_POST['id_cal_mahasiswa'])) {
        $id_cal_mahasiswa = $_POST['id_cal_mahasiswa'];
        $dat = $obj->deleteCalonMahasiswa($id_cal_mahasiswa); // Memanggil fungsi untuk menghapus data berdasarkan ID
        $msg = getJSON($dat); // Mengambil respons dalam format JSON
    }
}

// Mengambil data calon mahasiswa berdasarkan ID jika ada
$rows = $id_cal_mahasiswa ? $obj->getCalonMahasiswa($id_cal_mahasiswa) : [];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Data Calon Mahasiswa</title>
    <!-- Menyertakan Tailwind CSS dan Font Awesome -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        body {
            background-image: url('foto_pt.jpg'); /* Menambahkan gambar latar belakang */
            background-size: cover; /* Menyesuaikan ukuran gambar */
            background-position: center; /* Menyesuaikan posisi gambar */
            font-family: 'Arial', sans-serif;
        }
        .container {
            background-color: white;
            border-radius: 10px; /* Membuat sudut kontainer melengkung */
            border: 2px solid #3B82F6; /* Memberikan border biru */
        }
        .row-blue {
            background-color: #ebf4ff; /* Warna latar belakang biru muda untuk setiap baris */
        }
    </style>
</head>
<body class="bg-gray-100 p-6">

    <div class="max-w-4xl mx-auto p-6 rounded-lg shadow-md container">
        <h1 class="text-3xl font-bold mb-2 text-center text-blue-700">Calon Mahasiswa</h1> <!-- Judul Halaman -->
        <p class="text-gray-600 mb-4 text-center text-sm">Delete Data Calon Mahasiswa</p> <!-- Subjudul -->

        <!-- Menampilkan pesan sukses atau gagal -->
        <?php 
        if ($msg === true) { 
            echo '<div class="bg-green-500 text-white p-3 rounded mb-4">Delete Data Berhasil</div>'; // Pesan sukses
        } elseif ($msg === false) {
            echo '<div class="bg-red-500 text-white p-3 rounded mb-4">Delete Gagal</div>'; // Pesan gagal
        }
        ?>

        <form name="formDelete" method="POST" action="">
            <input type="hidden" name="submitted" value="1"/>
            
            <div class="space-y-4">
                <?php if (!empty($rows)) : ?>
                    <?php foreach ($rows as $row): ?>
                        <!-- Menampilkan informasi calon mahasiswa dalam baris -->
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">ID</span>
                            <span class="text-gray-600"><?php echo $row['id_cal_mahasiswa']; ?></span>
                        </div>
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">Nomor Registrasi</span>
                            <span class="text-gray-600"><?php echo $row['nomor_registrasi']; ?></span>
                        </div>
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">Nama</span>
                            <span class="text-gray-600"><?php echo $row['nama_cal_mahasiswa']; ?></span>
                        </div>
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">Jenis Kelamin</span>
                            <span class="text-gray-600"><?php echo $row['jk']; ?></span>
                        </div>
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">Tanggal Lahir</span>
                            <span class="text-gray-600"><?php echo $row['tanggal_lahir']; ?></span>
                        </div>
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">Sekolah Asal</span>
                            <span class="text-gray-600"><?php echo $row['sekolah_asal']; ?></span>
                        </div>
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">Jurusan</span>
                            <span class="text-gray-600"><?php echo $row['jurusan']; ?></span>
                        </div>
                        <div class="flex justify-between items-center row-blue p-2 rounded">
                            <span class="font-medium text-gray-700">Tahun Lulus</span>
                            <span class="text-gray-600"><?php echo $row['lulus_tahun']; ?></span>
                        </div>
                    <?php endforeach; ?>
                <?php else : ?>
                    <p class="text-gray-600">Data Calon Mahasiswa tidak ditemukan.</p>
                <?php endif; ?>
            </div>

            <!-- Input hidden untuk menyimpan ID Calon Mahasiswa -->
            <input type="hidden" name="id_cal_mahasiswa" value="<?php echo isset($row['id_cal_mahasiswa']) ? $row['id_cal_mahasiswa'] : ''; ?>" />

            <!-- Tombol aksi -->
            <div class="flex justify-between mt-4">
                <button type="submit" class="bg-red-500 text-white font-semibold py-2 px-4 rounded hover:bg-red-600">Delete</button>
                <a href="index.php" class="bg-gray-300 text-gray-800 font-semibold py-2 px-4 rounded hover:bg-gray-400">Cancel</a>
            </div>
        </form>
    </div>

</body>
</html>
