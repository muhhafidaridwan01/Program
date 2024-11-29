<?php
session_start();

# Periksa apakah inventaris sudah ada dalam sesi
if (!isset($_SESSION['inventaris'])) {
    $_SESSION['inventaris'] = array(
        "Pensil" => 100,
        "Buku" => 50,
        "Penghapus" => 75
    );
}
$inventaris = &$_SESSION['inventaris'];

# Fungsi untuk menambahkan barang ke dalam inventaris
function tambahBarang($nama, $kuantitas)
{
    global $inventaris;
    if (!isset($inventaris[$nama])) {
        $inventaris[$nama] = $kuantitas;
    } else {
        echo "<div class='alert alert-warning'>Barang $nama sudah ada di inventaris!</div>";
    }
}

# Fungsi untuk memperbarui kuantitas barang
function updateKuantitas($nama, $kuantitasBaru)
{
    global $inventaris;
    if (isset($inventaris[$nama])) {
        $inventaris[$nama] = $kuantitasBaru;
    } else {
        echo "<div class='alert alert-danger'>Barang $nama tidak ditemukan di inventaris!</div>";
    }
}

# Fungsi untuk menghapus barang dari inventaris
function hapusBarang($nama)
{
    global $inventaris;
    if (isset($inventaris[$nama])) {
        unset($inventaris[$nama]);
    } else {
        echo "<div class='alert alert-danger'>Barang $nama tidak ditemukan di inventaris!</div>";
    }
}

# Fungsi untuk menampilkan daftar inventaris
function tampilkanInventaris()
{
    global $inventaris;
    echo "<h3 class='text-center mb-3'>Daftar Inventaris:</h3>";
    if (count($inventaris) > 0) {
        echo "<ul class='list-group'>";
        foreach ($inventaris as $nama => $kuantitas) {
            echo "<li class='list-group-item'>Barang: <strong>$nama</strong>, Kuantitas: <strong>$kuantitas</strong></li>";
        }
        echo "</ul>";
    } else {
        echo "<div class='alert alert-info'>Inventaris kosong.</div>";
    }
}

# Cek apakah ada input dari pengguna
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['tambah'])) {
        tambahBarang($_POST['nama_barang'], $_POST['kuantitas']);
    } elseif (isset($_POST['update'])) {
        updateKuantitas($_POST['nama_barang'], $_POST['kuantitas']);
    } elseif (isset($_POST['hapus'])) {
        hapusBarang($_POST['nama_barang']);
    }
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manajemen Inventaris Barang</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="icon" type="image/x-icon" href="./assets/favicon.ico"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: 'Arial', sans-serif;
        }
        .card {
            border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            background-color: white;
            padding: 15px;
            margin-bottom: 15px;
        }
        .card h3 {
            font-size: 1.1rem;
            margin-bottom: 15px;
        }
        .form-group label {
            font-size: 0.85rem;
            margin-bottom: 5px;
        }
        .form-group input, .form-group button {
            font-size: 0.85rem;
            padding: 5px 10px;
        }
        .btn-primary, .btn-danger {
            font-size: 0.85rem;
            padding: 5px 15px;
            margin-top: 5px;
        }
        .list-group-item {
            font-size: 0.85rem;
            padding: 5px 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row">
            <!-- Bagian Kiri: Form -->
            <div class="col-md-5">
                <div class="card">
                    <h3><i class="fas fa-boxes"></i> Form Inventaris Barang</h3>

                    <!-- Form Tambah Barang -->
                    <form method="POST" class="mb-2">
                        <div class="form-group">
                            <label for="nama_barang">Nama Barang</label>
                            <input type="text" class="form-control" id="nama_barang" name="nama_barang" placeholder="Masukkan nama barang" required>
                        </div>
                        <div class="form-group">
                            <label for="kuantitas">Kuantitas</label>
                            <input type="number" class="form-control" id="kuantitas" name="kuantitas" placeholder="Masukkan kuantitas barang" required>
                        </div>
                        <button type="submit" name="tambah" class="btn btn-primary btn-block">Tambah</button>
                    </form>

                    <!-- Form Update Kuantitas Barang -->
                    <form method="POST" class="mb-2">
                        <div class="form-group">
                            <label for="nama_barang">Nama Barang</label>
                            <input type="text" class="form-control" name="nama_barang" placeholder="Masukkan nama barang" required>
                        </div>
                        <div class="form-group">
                            <label for="kuantitas">Kuantitas Baru</label>
                            <input type="number" class="form-control" name="kuantitas" placeholder="Masukkan kuantitas baru" required>
                        </div>
                        <button type="submit" name="update" class="btn btn-primary btn-block">Update</button>
                    </form>

                    <!-- Form Hapus Barang -->
                    <form method="POST">
                        <div class="form-group">
                            <label for="nama_barang">Nama Barang</label>
                            <input type="text" class="form-control" name="nama_barang" placeholder="Masukkan nama barang" required>
                        </div>
                        <button type="submit" name="hapus" class="btn btn-danger btn-block">Hapus</button>
                    </form>
                </div>
            </div>

            <!-- Bagian Kanan: Daftar Inventaris -->
            <div class="col-md-7">
                <div class="card">
                    <?php tampilkanInventaris(); ?>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
