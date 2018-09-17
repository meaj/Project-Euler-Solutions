"""
This program finds the number of viable routes, using only right and down turns, possible in an N by N grid
By Kevin Moore
"""


# Finds the factorial of a value n recursively
def factorial_recur(n):
    if (n == 0):
        return 1
    else:
        return n * factorial_recur(n-1)


# Finds the binomial coefficient of two values n and k
def n_choose_k(n, k):
    return factorial_recur(n)/(factorial_recur(k)*factorial_recur(n-k))


# finds the number of possible routes using only right and down turns in an N x N grid
def num_routes(int_n_val):
    return int(n_choose_k(int_n_val*2, int_n_val))


def main():
    int_n_val = int(input("Enter the size of the N by N grid: "))
    print(num_routes(int_n_val))

main()