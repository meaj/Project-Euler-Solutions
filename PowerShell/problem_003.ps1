# solution to problem 3 from projeteuler.net by meaj

function get-largestprimefactor {
    param([Parameter(ValueFromPipeline=$true)] $number)

    $maxval = [int64]([math]::Sqrt($number))

    while(($number % 2 -eq 0) -and ($number -ne 2)){ $number /= 2 }

    for ($i = 3;  $i -le $maxval; $i += 2){
        while(($number % $i -eq 0) -and ($number -ne $i)){ 
            $number = [int64]($number/$i) 
        }
    }
    return $number
}

get-largestprimefactor 13195

$tgt = 600851475143
get-largestprimefactor $tgt