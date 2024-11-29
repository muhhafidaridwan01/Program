<?php
function jumlahArray($array) {
    $total = 0;
    foreach ($array as $nilai) {
    $total += $nilai;
    }
    return $total;
    }
    $angka = [1, 2, 3, 4, 5];
    echo jumlahArray($angka); 
?>