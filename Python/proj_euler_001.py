# This program will find the sum of all multiples of five and three below 1000
# 
# By Kevin Moore

def main():
    sums = 0
    for i in range(0,1000):
        if (i % 3 == 0) and (i % 5 == 0):
            sums -= i
        if (i % 3 == 0):
            sums += i
        if (i % 5 == 0):
            sums += i
    print("The sum of all values divisble by 3 or 5 less than 1000 is " + str(sums))

main()
