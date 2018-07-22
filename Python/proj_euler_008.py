'''
This program finds the largest product of 13 consecutive digits of the 1000 digit number
By Kevin Moore
'''

str_number = "731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385" \
             "861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689" \
             "664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589" \
             "072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333" \
             "001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797" \
             "784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844" \
             "031998900088952434506585412275886668811642717147992444292823086346567481391912316282458617866458359124" \
             "566529476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245" \
             "544436298123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050" \
             "7754100225698315520005593572972571636269561882670428252483600823257530420752963450"

'''
Find Product function
Takes a string representing a series of digits and returns the product of said digits
'''
def find_product(str_number):
    int_product = 1
    # Determines the product of the digits in the substring
    for digit in str_number:
        int_product *= int(digit)
    return int_product

'''
Get Digits function
Takes one integer value int_size as input and returns the largest value substring of length int_size in big_number 
'''
def get_digits(int_size):
    # Verify the length of the number
    number_len = len(str_number)
    str_biggest_val = "0"
    # Advance the first digit in the 13 digit substring until the last possible substring is hit
    for place in range(0, number_len - int_size + 1):
        # Create substring
        str_test_val = str_number[place: place + int_size]
        # Verify the substring has a larger product and if not, update str_biggest_val
        if (find_product(str_test_val) > find_product(str_biggest_val)):
            str_biggest_val = str_test_val
    return str_biggest_val


def main():
    int_digits = 13
    str_max_value = get_digits(int_digits)
    int_product = find_product(str_max_value)
    print("The " + str(int_digits) + " digits with the largest product in the 1000 digit number are: " + str_max_value)
    print("The product of the digits is : " + str(int_product))

main()
