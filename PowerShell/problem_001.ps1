# solution to problem 1 from projeteuler.net by meaj

# do/while loop version
function get-doproblem001 {
    $sum = 0
    $i = 0
    do {
        if ($i % 3 -eq 0 -or $i % 5 -eq 0) {
            $sum += $i
        }
        $i++
    } while ($i -lt 1000)
    write-host "Sum of all numbers less than 1000 divisible by 3 or 5 is: $sum"
}

function get-forproblem001 {
    $sum = 0
    for ($i =0; $i -lt 1000; $i++){
        if ($i % 3 -eq 0 -or $i % 5 -eq 0) {
            $sum += $i
        }
    }
    write-host "Sum of all numbers less than 1000 divisible by 3 or 5 is: $sum"
}

$t = (measure-command {get-doproblem001}).ticks
write-host "ticks with do loop: $t`n"

$t = (measure-command {get-forproblem001}).ticks
write-host "ticks with for loop: $t`n"