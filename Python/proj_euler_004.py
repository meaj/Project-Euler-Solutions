import math

def main():
    for i in range(999,101,-1):
        for j in range(999,101,-1):
            x = str(i*j)
            if x == x[::-1]:
                print(x)

main()
