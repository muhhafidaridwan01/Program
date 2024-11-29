<?php
# array numerik sederhana
$warna = array("Merah", "Biru", "Hijau");
echo $warna[0]; # Output: Merah
echo "<br><br>";

# array dengan indeks numerik yang ditetapkan
$angka = array(1 => "Satu", 2 => "Dua", 3 => "Tiga");
echo $angka[2]; # Output: Dua
echo "<br><br>";

# array dengan angka sebagai elemen
$angka = array(10, 20, 30, 40, 50);
echo $angka[3]; # Output: 40
echo "<br><br>";

# array dengan elemen string
$buah = array("Apel", "Jeruk", "Mangga");
echo $buah[1]; # Output: Jeruk
echo "<br><br>";

# array dengan indeks otomatis
$hewan = array("Kucing", "Anjing", "Burung");
echo $hewan[2]; # Output: Burung
echo "<br><br>";

# menambahkan elemen ke array menggunakan array_push() 
$buah = array("Apel", "Pisang");
array_push($buah, "Mangga", "Jeruk");
print_r($buah); # Output: Array ( [0] => Apel [1] => Pisang [2] => Mangga[3] => Jeruk )
echo "<br><br>";

# mengubah indeks dalam array numerik
$angka = array(10, 20, 30);
$angka[1] = 25; # Mengubah elemen kedua menjadi 25
echo $angka[1]; # Output: 25
echo "<br><br>";

# mengubah foreach untuk iterasi array
$warna = array("Merah", "Biru", "Hijau");
foreach ($warna as $value) {
echo $value . " "; # Output: Merah Biru Hijau
}
echo "<br><br>";

# array numerik dengan elemen campuran
$data = array("Bola", "Sepakbola", "Tenis");
$data[3] = "Badminton"; # Menambahkan elemen baru dengan indeks 3
print_r($data); # Output: Array ( [0] => Bola [1] => Sepakbola [2] => Tenis [3] => Badminton )
echo "<br><br>";

# array numerik multidimensi
$kelas = array(
    array("Budi", "Andi"),
    array("Dewi", "Rani")
    );
    echo $kelas[1][0]; # Output: Dewi
?>