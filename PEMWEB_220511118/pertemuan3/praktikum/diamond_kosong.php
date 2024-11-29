<?php
$size = 4;
for ($i = 1; $i <= $size; $i++) {
    for ($j = $size - $i; $j > 0; $j--) {
        echo "&nbsp;";
    }
    for ($k = 1; $k <= (2 * $i - 1); $k++) {
        if ($k == 1 || $k == (2 * $i - 1)) {
            echo "*";
        } else {
            echo "&nbsp;";
        }
    }
    echo "<br>";
}
for ($i = $size - 1; $i >= 1; $i--) {
    for ($j = $size - $i; $j > 0; $j--) {
        echo "&nbsp;";
    }
    for ($k = 1; $k <= (2 * $i - 1); $k++) {
        if ($k == 1 || $k == (2 * $i - 1)) {
            echo "*";
        } else {
            echo "&nbsp;";
        }
    }
    echo "<br>";
}
?>
