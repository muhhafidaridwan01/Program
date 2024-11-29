<?php
 
 echo("<h3>Aplikasi Menghitung Luas dan Keliling Persegi Panjang</h3>");
 echo("<br/>");

 $panjang = $_POST['panjang'];
 $lebar = $_POST['lebar'];
 $luas = $panjang * $lebar;
 $kel = (2 * $panjang) + (2 * $lebar);

 // Output
 echo("Panjang:".$panjang);
 echo("<br/>");
 echo("Lebar:".$lebar);
 echo("<br/>");
 echo("Luas:".$luas);
 echo("<br/>");
 echo("Keliling:".$kel);
?>