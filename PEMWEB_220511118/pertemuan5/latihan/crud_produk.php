<?php
# array untuk menyimpan daftar produk dan harga
$produk = array(
    "Laptop" => 10000000,
    "Handphone" => 5000000,
    "TV" => 3000000
);

# fungsi untuk menambah produk
function tambahProduk($nama, $harga)
{
    global $produk;
    $produk[$nama] = $harga;
}

# fungsi untuk menghapus produk
function hapusProduk($nama)
{
    global $produk;
    if (isset($produk[$nama])) {
        unset($produk[$nama]);
    } else {
        echo "Produk tidak ditemukan.<br>";
    }
}

# fungsi untuk memperbarui harga produk
function updateHarga($nama, $hargaBaru)
{
    global $produk;
    if (isset($produk[$nama])) {
        $produk[$nama] = $hargaBaru;
    } else {
        echo "Produk tidak ditemukan.<br>";
    }
}

# menampilkan daftar produk
function tampilkanProduk()
{
    global $produk;
    echo "<h3>Daftar Produk:</h3>";
    foreach ($produk as $nama => $harga) {
        echo "Produk: $nama, Harga: Rp " . number_format($harga, 0, ',', '.')
            . "<br>";
    }
}

# cek apakah ada input dari pengguna (simulasi form submission)
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['tambah'])) {
        # menambah produk
        tambahProduk($_POST['produk'], $_POST['harga']);
    } elseif (isset($_POST['hapus'])) {
        # menghapus produk
        hapusProduk($_POST['produk']);
    } elseif (isset($_POST['update'])) {
        # memperbarui harga produk
        updateHarga($_POST['produk'], $_POST['harga']);
    }
}

# menampilkan produk terbaru setelah operasi  
tampilkanProduk();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Belanja Produk</title>
</head>

<body>
    <h1>Daftar Belanja Produk</h1>
    <form method="POST">
        <h3>Tambah Produk Baru</h3>
        Nama Produk: <input type="text" name="produk" required><br>
        Harga Produk: <input type="number" name="harga" required><br>
        <button type="submit" name="tambah">Tambah Produk</button>
    </form>
    <form method="POST">
        <h3>Hapus Produk</h3>
        Nama Produk: <input type="text" name="produk" required><br>
        <button type="submit" name="hapus">Hapus Produk</button>
    </form>
    <form method="POST">
        <h3>Update Harga Produk</h3>
        Nama Produk: <input type="text" name="produk" required><br>
        Harga Baru: <input type="number" name="harga" required><br>
        <button type="submit" name="update">Update Harga</button>
    </form>
</body>
</html>