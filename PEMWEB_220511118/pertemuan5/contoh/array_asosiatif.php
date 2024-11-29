<?php
# array asosiatif sederhana
$harga_buah = array("Apel" => 5000, "Jeruk" => 7000, "Mangga" => 6000);
echo $harga_buah["Jeruk"]; # Output: 7000
echo "<br><br>";

# array asosiatif dengan auknci string dan nilai numerik
$umur = array("John" => 25, "Doe" => 30, "Jane" => 22);
echo $umur["Doe"]; # Output: 30
echo "<br><br>";

# array asosiatif dengan nilai array
$kontak = array(
"John" => array("email" => "john@example.com", "telepon" =>
"123456789"),
"Doe" => array("email" => "doe@example.com", "telepon" => "987654321")
);
echo $kontak["John"]["email"]; # Output: john@example.com
echo "<br><br>";

# menambahkan elemen ke array asosiatif
$produk = array("Laptop" => 15000000, "Handphone" => 5000000);
$produk["Tablet"] = 3500000;
print_r($produk); # Output: Array ( [Laptop] => 15000000 [Handphone] => 5000000 [Tablet] => 3500000 )
echo "<br><br>";

# mengubah nilai elemen dalam array asosiatif
$harga_barang = array("Baju" => 100000, "Sepatu" => 150000);
$harga_barang["Baju"] = 120000; # Mengubah harga Baju menjadi 120000
echo $harga_barang["Baju"]; # Output: 120000
echo "<br><br>";

# array asosiatif dengan kunci tipe lain (integer)
$produk = array(1 => "Susu", 2 => "Teh", 3 => "Kopi");
echo $produk[2]; # Output: Teh
echo "<br><br>";

# menggunakan foreach untuk iterasi array asosiatif
$siswa = array("Nama" => "Budi", "Usia" => 20, "Kelas" => "A");
foreach ($siswa as $key => $value) {
echo $key . ": " . $value . "\n"; # Output: Nama: Budi, Usia: 20, Kelas: A
}
echo "<br><br>";

# array asosiatif dengan data campuran
$karyawan = array(
"ID" => 101,
"Nama" => "Budi",
"Posisi" => "Manager",
"Gaji" => 7000000
);
echo $karyawan["Nama"]; # Output: Budi
echo "<br><br>";

# array asosiatif dengan menggunakan array_merge() 
$array1 = array("A" => "Merah", "B" => "Biru");
$array2 = array("C" => "Hijau", "D" => "Kuning");
$hasil = array_merge($array1, $array2);
print_r($hasil); # Output: Array ( [A] => Merah [B] => Biru [C] => Hijau [D] => Kuning )
echo "<br><br>"; 

# array asosiatif dengan fungsi array_keys() dan array_values() 
$produk = array("Laptop" => 15000000, "Handphone" => 5000000);
$kunci = array_keys($produk); # Mengambil kunci array
$nilai = array_values($produk); # Mengambil nilai array
print_r($kunci); # Output: Array ( [0] => Laptop [1] => Handphone )
print_r($nilai); # Output: Array ( [0] => 15000000 [1] => 5000000 )
?>