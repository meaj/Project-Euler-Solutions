"""
This program recursively finds the longest Collatz sequence with a starting value less than 1000000
By Kevin Moore
"""

import sys
sys.setrecursionlimit(15000)

# Holds known collatz chain lengths to save on calculaitons
dct_chain_lens = {}

# Recursively calculates length of collatz chains unless the length of a given value is known
def collatz_recur(int_val, int_steps):
    # Preform calculations if values not in dictionary
    if not int_val in dct_chain_lens:
        # Base case
        if (int_val == 1):
            return int_steps
        # Even recursive case
        if (int_val % 2 == 0):
            return collatz_recur(int_val/2, int_steps+1)
        # Odd recursive case
        elif (int_val% 2 == 1):
            return collatz_recur((int_val*3)+1, int_steps+1)
    # Add current number of steps to the known number of steps in the chain
    else:
        return int_steps+dct_chain_lens[int_val]

def show_collatz_chain(lst_test_chain):
    # Base case
    if (lst_test_chain[-1] == 1):
        return lst_test_chain
    # Even recursive case
    if (lst_test_chain[-1] % 2 == 0):
        lst_test_chain.append(int(lst_test_chain[-1] / 2))
        return show_collatz_chain(lst_test_chain)
    # Odd recursive case
    elif (lst_test_chain[-1] % 2 == 1):
        lst_test_chain.append(int((lst_test_chain[-1] *3) + 1))
        return show_collatz_chain(lst_test_chain)

def main():
    lst_chain = []
    int_max_val = 0
    int_max_steps = 0
    # Search for longest collatz chain less than 1,000,000
    for i in range(1, 1000001):
        print("Testing value " + str(i))
        int_steps = collatz_recur(i, 1)
        dct_chain_lens[i] = int_steps
        if int_steps > int_max_steps:
            int_max_steps = int_steps
            int_max_val = i

    lst_chain.append(int_max_val)
    lst_chain = show_collatz_chain(lst_chain)
    print("\n\nMaximum value: " + str(int_max_val))
    print("Chain: ")
    print(lst_chain)

main()