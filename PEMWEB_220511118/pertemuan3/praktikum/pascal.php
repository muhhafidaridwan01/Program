<?php
function printPascalsTriangle($n) {
    for ($line = 0; $line < $n; $line++) {
        $num = 1; 
        echo str_repeat("&nbsp;", $n - $line); 

        for ($i = 0; $i <= $line; $i++) {
            echo $num . "&nbsp;&nbsp;"; 
            $num = $num * ($line - $i) / ($i + 1);
        }
        echo "<br>"; 
    }
}

$rows = 4; 
printPascalsTriangle($rows);
?>
