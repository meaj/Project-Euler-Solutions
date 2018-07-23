'''
This program will find the largest palindrome formed by three digit numbers
By Kevin Moore
'''

'''
Iterative Palindrome Over Range function
Returns a list of palindromes formed by all values in the range int_a to int_b
'''
def iterative_palindromes(int_a, int_b):
    palindromes = []
    # iterate backwards through the range from int_a to int_b
    for i in range(int_b, int_a, -1):
        for j in range(int_b, int_a, -1):
            x = i * j
            # if the string version of x is the same forwards as backwards, add it to the palindrome list
            if str(x) == str(x)[::-1]:
                palindromes.append(x)
    return palindromes

def main():
    print(max(iterative_palindromes(101,999)))

main()
