<?php
$size = 4;
$num = 1;
for ($i = 1; $i <= $size; $i++) {
    for ($j = 1; $j <= $i; $j++) {
        echo $num++ . " ";
    }
    echo "<br>";
}
?>
