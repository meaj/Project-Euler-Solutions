# solution to problem 2 from projeteuler.net by meaj

$max = 4000000
$i =1
$n = 2
$sum = 0

while($n -lt $max){
    if ($n % 2 -eq 0){
        $sum += $n
    }
    $n = $n + $i
    $i = $n - $i
}

write-host "sum of all fib numbers less than $max is $sum"