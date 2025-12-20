<?php

$number = 5;
$string = strval($number);

if (str_contains($string, '1')) {
    echo "Number is 1\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";
    }
}

if (str_contains($string, '2')) {
    echo "Number is 2\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";
    }
}

if (str_contains($string, '3')) {
    echo "Number is 3\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";
    }
}

if (str_contains($string, '4')) {
    echo "Number is 4\n";
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";
    }
}

if (str_contains($string, '5')) {
    echo "Bingo! Number is 5\n";
	echo "And 5*5 is ";
	eval('echo ' . ($number * $number) . ';'); 
    for ($i = 0; $i < $number; $i++) {
        echo "Loop iteration: $i\n";
    }
}

?>