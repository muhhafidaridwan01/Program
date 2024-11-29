<?php
# array multidimensi dengan indeks numerik
$matriks = array(
array(1, 2, 3),
array(4, 5, 6),
array(7, 8, 9)
);
echo $matriks[1][2]; # Output: 6
echo "<br><br>";

# array multidimensi dengan indeks asosiatif
$siswa = array(
"John" => array("Usia" => 20, "Kelas" => "A"),
"Doe" => array("Usia" => 22, "Kelas" => "B")
);
echo $siswa["Doe"]["Usia"]; # Output: 22
echo "<br><br>";

# matriks 3x3
$matriks = array(
array(1, 2, 3),
array(4, 5, 6),
array(7, 8, 9)
);
echo $matriks[2][1]; # Output: 8
echo "<br><br>";

# array multidimensi dengan data campuran
$data = array(
"orang1" => array("Nama" => "Budi", "Umur" => 25),
"orang2" => array("Nama" => "Andi", "Umur" => 30)
);
echo $data["orang1"]["Nama"]; # Output: Budi
echo "<br><br>";

# array multidimensi dengan indeks numerik dan asosiatif
$produk = array(
"Laptop" => array("Harga" => 10000000, "Stok" => 50),
"Handphone" => array("Harga" => 5000000, "Stok" => 100)
);
echo $produk["Handphone"]["Harga"]; # Output: 5000000
echo "<br><br>";

# array multidimensi dengan data angka
$nilai = array(
array(75, 80, 85),
array(70, 75, 78),
array(90, 88, 85)
);
echo $nilai[2][0]; # Output: 90
echo "<br><br>";

# array multidimensi dengan penggunaan foreach 
$produk = array(
array("ID" => 1, "Nama" => "Laptop", "Harga" => 10000000),
array("ID" => 2, "Nama" => "Handphone", "Harga" => 5000000)
);
foreach ($produk as $item) {
echo $item["Nama"] . ": " . $item["Harga"] . "\n";
}
# Output:
# Laptop: 10000000
# Handphone: 5000000
echo "<br><br>";

# matriks 2x2 dengan data asosiatif
$matriks = array(
"baris1" => array("A" => 1, "B" => 2),
"baris2" => array("A" => 3, "B" => 4)
);
echo $matriks["baris1"]["A"]; # Output: 1
echo "<br><br>";

# array multidimensi dengan data pribadi
$karyawan = array(
array("Nama" => "Budi", "Jabatan" => "Manager", "Gaji" => 5000000),
array("Nama" => "Andi", "Jabatan" => "Staff", "Gaji" => 3000000)
);
echo $karyawan[1]["Jabatan"]; # Output: Staff
echo "<br><br>";

# array multidimensi untuk menyimpan jadwal pelajaran
$jadwal = array(
"Senin" => array("Matematika", "Bahasa Indonesia", "IPA"),
"Selasa" => array("Bahasa Inggris", "Sejarah", "Pendidikan Agama"),
"Rabu" => array("Seni", "Olahraga", "Matematika")
);
echo $jadwal["Senin"][2]; # Output: IPA
?>