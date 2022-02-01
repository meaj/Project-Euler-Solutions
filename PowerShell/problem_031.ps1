$value = 200
$coins = @(1, 2, 5, 10, 20, 50, 100, 200)
$table = new-object int[] ($value + 1)

# one way to make change with 1u coins
$table[0] = 1
# fill up the table for each coin type
for ($i = 0; $i -lt $coins.Length; $i++){
    #lookup old values for lower unit coins than $i and add up to target value
    for ($j = $coins[$i]; $j -le $value; $j++){
        $table[$j] += $table[$j - $coins[$i]]
    }
}
write-host $table[$table.Length-1]