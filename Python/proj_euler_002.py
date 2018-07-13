# This program will the sum of all Fibonacci numbers below 4000000
# By Kevin Moore

def main():
    sums = 0
    tmp = 0
    lo = 1
    hi = 2
    while hi <= 4000000:
        tmp = hi
        hi = tmp + lo
        lo = tmp

        if lo % 2 == 0:
            sums += lo
    print("The sum of all even fibonacci numbers less than 400000 is " + str(sums))
main()
