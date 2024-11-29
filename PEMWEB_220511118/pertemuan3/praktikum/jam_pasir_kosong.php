<?php
$lebar_pola = 4;

for ($i = 0; $i < $lebar_pola; $i++) {
    for ($j = 0; $j < $i; $j++) {
        echo "&nbsp;&nbsp;";
    }

    for ($k = 0; $k < $lebar_pola - $i; $k++) {
        if ($i == 0 || $k == 0 || $k == $lebar_pola - $i - 1) {
            echo "*&nbsp; ";
        } else {
            echo "&nbsp;&nbsp;&nbsp;&nbsp;";
        }
    }
    echo "<br>";
}

for ($i = $lebar_pola - 2; $i >= 0; $i--) {
    for ($j = 0; $j < $i; $j++) {
        echo "&nbsp;&nbsp;";
    }

    for ($k = 0; $k < $lebar_pola - $i; $k++) {
        if ($i == 0 || $k == 0 || $k == $lebar_pola - $i - 1) {
            echo "*&nbsp;&nbsp;";
        } else {
            echo "&nbsp;&nbsp;&nbsp;&nbsp";
        }
    }
    echo "<br>";
}
?>
