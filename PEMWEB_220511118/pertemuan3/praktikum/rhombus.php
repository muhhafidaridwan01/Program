<?php
$rows = 5; 
$cols = 4; 

for ($i = 0; $i < $rows; $i++) {
    for ($j = 0; $j < $i; $j++) {
        echo "&nbsp;";
    }

    for ($k = 0; $k <$cols; $k++) {
        echo "* ";
    }

    echo "<br>";

}