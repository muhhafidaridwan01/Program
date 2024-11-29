<?php
// Menyertakan file controller untuk calon mahasiswa
include("../controllers/CalonMahasiswa.php"); 

// Menyertakan file library untuk fungsi tambahan
include("../lib/functions.php"); 

// Membuat objek CalonMahasiswaController untuk mengelola data calon mahasiswa
$obj = new CalonMahasiswaController(); 

// Variabel untuk menyimpan pesan yang akan ditampilkan di halaman
$msg = null; 

// Memproses form jika ada data POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Menangkap data dari form input
    $nomor_registrasi = $_POST["nomor_registrasi"];
    $nama_cal_mahasiswa = $_POST["nama_cal_mahasiswa"];
    $jk = $_POST["jk"];
    $tanggal_lahir = $_POST["tanggal_lahir"];
    $sekolah_asal = $_POST["sekolah_asal"];
    $jurusan = $_POST["jurusan"];
    $lulus_tahun = $_POST["lulus_tahun"];
    
    // Menyimpan data ke database melalui controller
    $dat = $obj->addCalonMahasiswa($nomor_registrasi, $nama_cal_mahasiswa, $jk, $tanggal_lahir, $sekolah_asal, $jurusan, $lulus_tahun);
    
    // Menentukan pesan berdasarkan hasil penyimpanan data
    if ($dat) {
        $msg = 'Insert Data Berhasil'; // Pesan jika penyimpanan berhasil
    } else {
        $msg = 'Insert Gagal'; // Pesan jika penyimpanan gagal
    }
}
?>

<html>
<head>
    <title>Calon Mahasiswa</title> <!-- Judul halaman -->
    
    <!-- Menyertakan CDN Tailwind CSS untuk styling -->
    <script src="https://cdn.tailwindcss.com"></script> 
    
    <!-- Menyertakan CDN Font Awesome untuk ikon -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"> 
    
    <script>
        // Fungsi untuk mengosongkan input form
        function clearForm() {
            document.forms["formAdd"].reset(); // Mereset semua input form
        }

        // Fungsi untuk menyembunyikan pesan setelah 3 detik
        function hideMessage() {
            setTimeout(function() {
                var messageElement = document.getElementById('message');
                if (messageElement) {
                    messageElement.style.display = 'none'; // Menghilangkan pesan
                }
            }, 3000); // Setelah 3 detik
        }
    </script>
</head>
<body class="bg-cover bg-center bg-fixed" style="background-image: url('sekolahan.JPG');"> <!-- Menampilkan latar belakang gambar -->
    <div class="flex justify-center items-center h-screen"> <!-- Menempatkan form di tengah halaman -->
        
        <!-- Form untuk input data -->
        <div class="max-w-sm w-full bg-white rounded-lg shadow-lg p-2 ml-[200px]">
            <h1 class="text-xl font-semibold text-center mb-3">Calon Mahasiwa</h1> <!-- Judul form -->
            <p class="text-gray-600 text-center mb-4 text-sm">Entry Data</p> <!-- Keterangan -->

            <!-- Menampilkan pesan status berdasarkan penyimpanan data -->
            <?php if ($msg): ?>
                <div id="message" class="bg-<?php echo ($msg == 'Insert Data Berhasil') ? 'green' : 'red'; ?>-500 text-white p-3 rounded mb-4 text-center text-xs">
                    <?php echo $msg; ?>
                </div>
                <script>
                    hideMessage(); // Menyembunyikan pesan setelah beberapa detik
                </script>
            <?php endif; ?>

            <!-- Form input calon mahasiswa -->
            <form name="formAdd" method="POST" action="">
                <div class="mb-3">
                    <label for="nomor_registrasi" class="block text-xs font-medium text-gray-700">Nomor Registrasi</label>
                    <input type="number" id="nomor_registrasi" name="nomor_registrasi" placeholder="Masukkan Nomor Registrasi" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                </div>
                <div class="mb-3">
                    <label for="nama_cal_mahasiswa" class="block text-xs font-medium text-gray-700">Nama Calon Mahasiswa</label>
                    <input type="text" id="nama_cal_mahasiswa" name="nama_cal_mahasiswa" placeholder="Masukkan Nama Mahasiswa" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                </div>
                <div class="mb-3">
                    <label for="jk" class="block text-xs font-medium text-gray-700">Jenis Kelamin</label>
                    <select id="jk" name="jk" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required>
                        <option value="">--Pilih Jenis Kelamin--</option>
                        <option value="L">Laki-laki</option>
                        <option value="P">Perempuan</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="tanggal_lahir" class="block text-xs font-medium text-gray-700">Tanggal Lahir</label>
                    <input type="date" id="tanggal_lahir" name="tanggal_lahir" placeholder="Masukkan Tanggal Lahir" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                </div>
                <div class="mb-3">
                    <label for="sekolah_asal" class="block text-xs font-medium text-gray-700">Asal Sekolah</label>
                    <input type="text" id="sekolah_asal" name="sekolah_asal" placeholder="Masukkan Asal Sekolah" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                </div>
                <div class="mb-3">
                    <label for="jurusan" class="block text-xs font-medium text-gray-700">Jurusan</label>
                    <input type="text" id="jurusan" name="jurusan" placeholder="Masukkan Jurusan" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                </div>
                <div class="mb-3">
                    <label for="lulus_tahun" class="block text-xs font-medium text-gray-700">Tahun Lulus</label>
                    <input type="text" id="lulus_tahun" name="lulus_tahun" placeholder="Masukkan Tahun Lulus" class="mt-1 block w-full border-2 border-blue-300 rounded-md shadow-sm focus:ring focus:ring-blue-500 p-1.5 text-xs" required />
                </div>
                <div class="flex justify-between">
                    <button class="bg-blue-500 text-white font-semibold py-2 px-4 rounded hover:bg-blue-600 text-xs" type="submit">Save</button>
                    <button type="button" onclick="clearForm()" class="bg-gray-300 text-gray-800 font-semibold py-2 px-4 rounded hover:bg-gray-400 text-xs">Clear</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
