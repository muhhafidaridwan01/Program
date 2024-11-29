<?php
function fibonacci($n) {
    $a = 0;
    $b = 1;
    $result = [$a, $b];
    for ($i = 2; $i < $n; $i++) {
    $c = $a + $b;
    $result[] = $c;
    $a = $b;
    $b = $c;
    }
    return $result;
    }
    print_r(fibonacci(5));
?>