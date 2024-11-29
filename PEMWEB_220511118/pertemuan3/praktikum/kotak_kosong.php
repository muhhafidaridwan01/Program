<?php
$size = 5;
for ($i = 1; $i <= $size; $i++) {
    for ($j = 1; $j <= $size; $j++) {
        if ($i == 1 || $i == $size || $j == 1 || $j == $size) {
            echo "*";
        } else {
            echo "&nbsp;&nbsp;";
        }
    }
    echo "<br>";
}
?>
