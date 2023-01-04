<?php

$s = rand(1, 100);
$w = 0;

while (true) {
    $t = (int) readline("1 ile 100 arasında tahmininizi giriniz : ");
    if ($t == $s) {
        echo "Doğru tahmin. Tahmin sayınız $w, doğru sayı $s\n";
        break;
    } else if ($t < $s) {
        echo "Lütfen daha büyük bir sayı giriniz\n";
        $w++;
        if ($w > 9) {
            echo "Maksimum yanlış sayısına ulaştınız.\n";
            break;
        } else {
            continue;
        }
    } else if ($t > $s) {
        echo "Lütfen daha küçük bir sayı giriniz\n";
        $w++;
        if ($w > 9) {
            echo "Maksimum yanlış sayısına ulaştınız.\n";
            break;
        } else {
            continue;
        }
    } else {
        echo "Geçersiz İşlem\n";
    }
}

