import math

def main():
    x = int(input("Enter a number: "))
    for i in range(3,x+1):
        for j in range(2, int(math.sqrt(x)+1)):
            if x % j == 0:
                continue
            if x % j != 0:
                print(x)
        

main()
