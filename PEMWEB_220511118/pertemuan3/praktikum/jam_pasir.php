<?php
$size = 4;

for ($i = $size; $i >= 1; $i--) {
    for ($j = $size - $i; $j > 0; $j--) {
        echo "&nbsp;&nbsp;"; 
    }
    for ($k = 1; $k <= (1 * $i); $k++) {
        echo "*&nbsp;&nbsp;"; 
    }
    echo "<br>";
}

for ($i = 2; $i <= $size; $i++) {
    for ($j = $size - $i; $j > 0; $j--) {
        echo "&nbsp;&nbsp;"; 
    }
    for ($k = 1; $k <= (1 * $i); $k++) {
        echo "*&nbsp;&nbsp;";
    }
    echo "<br>";
}
?>
