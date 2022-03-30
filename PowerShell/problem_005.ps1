# solution to problem 5 from projecteuler.net by meaj
function get-factorial ($val){
    if ($val -eq 0){
        $r = 1
    } else {
        $r = [int64] ((get-factorial ($val-1)) * $val)
    }
    return $r
}

function get-smallestdivisiblenumber ($range){
    $val = get-factorial $range
    for ($c = 1; $c -le $val; $c++){
        $i = 1
        $cnt = 1
        while ($cnt -eq 1){
            if (($c % $i -eq 0) -and ($i -le $range)) {
                $i++
            } elseif ($i -gt $range) {
                $cnt = $c
            } else {
                $cnt = 0
            }
        }
        if (($cnt -lt $val) -and ($cnt -ne 0)){
            $val = $c
        }
    }
    Write-Host "$val"
}

Write-Host (measure-command {get-smallestdivisiblenumber 10}).TotalSeconds
Write-Host (measure-command {get-smallestdivisiblenumber 20}).TotalSeconds