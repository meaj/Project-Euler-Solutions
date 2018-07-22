'''
This program finds the pythagorean triplet for which a + b + c = 1000
By Kevin Moore
'''

'''
Find Pythagorean Triplet function
This function will find a pythagorean triplet that adds up to the value of int_n, and return the three values
'''
def find_triplet(int_n):
    # we only need to go from 1 to n/3 to satisfy a<b<C
    for int_a in range (1, int_n//3):
        # formula for b derived from N^2=(a+b+c)^2 and a^2+b^2=c^2
        int_b = (2 * int_a * int_n - int_n ** 2) // (2 * (int_a - int_n))
        # formula for c derived from N=a+b+c
        int_c = int_n - int_a - int_b
        # verify a<b<c and a^2+b^2=c^2
        if (int_a < int_b < int_c and int_a**2 + int_b**2 == int_c**2):
            return int_a, int_b, int_c
    # return value in case that no triple is found
    return -1, -1, -1


def main():
    int_n = 1000
    a, b, c = find_triplet(int_n)
    if (a == -1):
        print("No triplet found")
    else:
        print("The pythagorean triplet "+ str(a) +  ", " + str(b) + ", " + str(c) + " adds together to equal " + str(int_n))
        print("The product of this triplet is " + str(a*b*c))

main()
