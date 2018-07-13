# This program will the sum of all Fibonacci numbers
# below 4000000
# By Meaj

def main():
    sums = 0
    a = 1
    b = 1
    while a <= 4000000 and b <= 4000000:
        a = a+b
        print(a)
        b = b + a
        print(b)
        
        if a % 2 == 0:
            sums += a
        if b % 2 == 0:
            sums += b
    print(sums)

main()
