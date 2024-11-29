<?php
// Memasukkan file controller dan fungsi tambahan
include("../controllers/CalonMahasiswa.php");
include("../lib/functions.php");

// Membuat objek controller untuk CalonMahasiswa
$obj = new CalonMahasiswaController();

// Mengecek apakah ada parameter id_cal_mahasiswa yang dikirimkan melalui URL
if (isset($_GET["id_cal_mahasiswa"])) {
    $id_cal_mahasiswa = $_GET["id_cal_mahasiswa"];
} else {
    // Jika tidak ada, arahkan pengguna ke halaman edit.php
    header("Location: edit.php"); // Ganti dengan halaman yang sesuai
    exit; // Menghentikan eksekusi script setelah redirect
}

$msg = null; // Inisialisasi pesan kosong

// Mengecek apakah form telah disubmit (POST)
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Mengambil data dari form
    $nomor_registrasi = $_POST["nomor_registrasi"];
    $nama_cal_mahasiswa = $_POST["nama_cal_mahasiswa"];
    $jk = $_POST["jk"];
    $tanggal_lahir = $_POST["tanggal_lahir"];
    $sekolah_asal = $_POST["sekolah_asal"];
    $jurusan = $_POST["jurusan"];
    $lulus_tahun = $_POST["lulus_tahun"];
    
    // Memanggil fungsi untuk melakukan update data calon mahasiswa
    $dat = $obj->updateCalonMahasiswa($id_cal_mahasiswa, $nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun);

    // Mengecek apakah update berhasil
    if ($dat) {
        $msg = 'Update Data Berhasil'; // Menampilkan pesan sukses
    } else {
        $msg = 'Update Gagal'; // Menampilkan pesan gagal
    }
}

// Mengambil data calon mahasiswa yang akan diedit
$rows = $obj->getCalonMahasiswa($id_cal_mahasiswa);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Calon Mahasiswa</title>
    <!-- Memasukkan TailwindCSS untuk styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        // Fungsi untuk menampilkan pesan sukses atau gagal selama 3 detik
        window.onload = function() {
            var msg = document.getElementById('msg');
            if (msg) {
                setTimeout(function() {
                    msg.style.display = 'none'; // Menyembunyikan pesan setelah 3 detik
                }, 3000);
            }
        };
    </script>
</head>
<body class="bg-cover bg-center bg-fixed" style="background-image: url('sekolahan.jpg');">
    <!-- Kontainer utama, memposisikan form di tengah layar -->
    <div class="flex justify-center items-center min-h-screen">
        <!-- Form untuk mengedit data calon mahasiswa -->
        <div class="max-w-xs w-full bg-white rounded-lg shadow-lg p-4">
            <h1 class="text-xl font-semibold text-center mb-3">Edit Calon Mahasiswa</h1>
            <p class="text-gray-600 text-center mb-4 text-sm">Perbarui Data Calon Mahasiswa</p>

            <!-- Menampilkan pesan setelah proses update -->
            <?php 
            if (isset($msg)) {
                echo '<div id="msg" class="bg-green-500 text-white p-3 rounded mb-4 text-center text-xs">' . $msg . '</div>';
            }
            ?>

            <!-- Form untuk mengedit data calon mahasiswa -->
            <form name="formEdit" method="POST" action="">
                <input type="hidden" name="submitted" value="1"/>
                <?php if ($rows) { $row = $rows[0]; ?>
                    <!-- Input ID Calon Mahasiswa (readonly) -->
                    <div class="mb-3">
                        <label for="id_cal_mahasiswa" class="block text-xs font-medium text-gray-700">ID</label>
                        <input type="text" id="id_cal_mahasiswa" name="id_cal_mahasiswa" value="<?php echo $row['id_cal_mahasiswa']; ?>" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" readonly />
                    </div>

                    <!-- Input Nomor Registrasi -->
                    <div class="mb-3">
                        <label for="nomor_registrasi" class="block text-xs font-medium text-gray-700">No. Registrasi</label>
                        <input type="number" id="nomor_registrasi" name="nomor_registrasi" value="<?php echo $row['nomor_registrasi']; ?>" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                    </div>

                    <!-- Input Nama Calon Mahasiswa -->
                    <div class="mb-3">
                        <label for="nama_cal_mahasiswa" class="block text-xs font-medium text-gray-700">Nama</label>
                        <input type="text" id="nama_cal_mahasiswa" name="nama_cal_mahasiswa" value="<?php echo $row['nama_cal_mahasiswa']; ?>" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                    </div>

                    <!-- Pilih Jenis Kelamin -->
                    <div class="mb-3">
                        <label for="jk" class="block text-xs font-medium text-gray-700">JK</label>
                        <select name="jk" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required>
                            <option value="L" <?php if ($row['jk'] == 'L') echo 'selected'; ?>>Laki-Laki</option>
                            <option value="P" <?php if ($row['jk'] == 'P') echo 'selected'; ?>>Perempuan</option>
                        </select>
                    </div>

                    <!-- Input Tanggal Lahir -->
                    <div class="mb-3">
                        <label for="tanggal_lahir" class="block text-xs font-medium text-gray-700">Tanggal Lahir</label>
                        <input type="date" id="tanggal_lahir" name="tanggal_lahir" value="<?php echo $row['tanggal_lahir']; ?>" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                    </div>

                    <!-- Input Sekolah Asal -->
                    <div class="mb-3">
                        <label for="sekolah_asal" class="block text-xs font-medium text-gray-700">Sekolah Asal</label>
                        <input type="text" id="sekolah_asal" name="sekolah_asal" value="<?php echo $row['sekolah_asal']; ?>" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                    </div>

                    <!-- Input Jurusan -->
                    <div class="mb-3">
                        <label for="jurusan" class="block text-xs font-medium text-gray-700">Jurusan</label>
                        <input type="text" id="jurusan" name="jurusan" value="<?php echo $row['jurusan']; ?>" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                    </div>

                    <!-- Input Tahun Lulus -->
                    <div class="mb-3">
                        <label for="lulus_tahun" class="block text-xs font-medium text-gray-700">Tahun Lulus</label>
                        <input type="number" id="lulus_tahun" name="lulus_tahun" value="<?php echo $row['lulus_tahun']; ?>" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                    </div>

                    <!-- Tombol Submit -->
                    <div class="flex justify-center">
                        <button type="submit" class="bg-blue-500 text-white rounded-md py-2 px-4 text-xs">Perbarui</button>
                    </div>
                <?php } ?>
            </form>
        </div>
    </div>
</body>
</html>
