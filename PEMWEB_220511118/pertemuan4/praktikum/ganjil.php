<?php
function cekGanjilGenap($angka) {
return ($angka % 2 == 0) ? "Genap" : "Ganjil";
}
echo cekGanjilGenap(7); 
?>