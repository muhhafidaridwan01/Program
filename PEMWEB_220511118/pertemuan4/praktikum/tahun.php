<?php
function cekTahunKabisat($tahun) {
    if (($tahun % 4 == 0 && $tahun % 100 != 0) || $tahun % 400 == 0) {
    return "Tahun kabisat";
    } else {
    return "Bukan tahun kabisat";
    }
    }
    echo cekTahunKabisat(2024);
?>