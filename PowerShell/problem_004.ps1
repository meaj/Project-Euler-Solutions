# solution to problem 4 from projecteuler.net by meaj
function get-ispalindrome ($val){
    $str = $val.tostring()
    $len = ($str).length
    for ($i = 0; $i -lt $len/2; $i++){
        if ($str[$i] -ne $str[$len-$i-1]){
            return $false
        }
    }
    return $true
}

function get-maxpalindrome ($start, $stop){
    $max = 0
    for ($i = $start; $i -le $stop; $i++){
        for ($j = $start; $j -le $stop; $j++){
            $v = $i * $j
            if ((get-ispalindrome $v) -and ($v -gt $max)){
                $max = $v
            }
        }
    }
    Write-Host "largest palindrome between $start and $stop is $max `nsec taken: " -NoNewline
    return $max
}

Write-Host (measure-command {get-maxpalindrome 10 99}).TotalSeconds
Write-Host (measure-command {get-maxpalindrome 90 99}).TotalSeconds

Write-Host (measure-command {get-maxpalindrome 100 999}).TotalSeconds
Write-Host (measure-command {get-maxpalindrome 900 999}).TotalSeconds

Write-Host (measure-command {get-maxpalindrome 9000 9999}).TotalSeconds