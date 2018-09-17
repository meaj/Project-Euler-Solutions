"""
This program finds the number of letters used to write out in words the numbers 1 to the value specified by the user
By Kevin Moore
"""

lst_0_to_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

lst_tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def form_string(int_value):
    if int_value < 20:
        str_out = lst_0_to_19[int_value]
    elif int_value < 100:
        str_out = lst_tens[int_value // 10] + form_string(int_value%10)
    elif int_value < 1000:
        str_out = lst_0_to_19[int_value//100] + "hundred"
        if int_value%100 != 0:
            str_out += "and" + form_string(int_value%100)
    elif int_value < 100000:
        str_out = form_string(int_value//1000) + "thousand" + form_string(int_value%1000)
    elif int_value == 1000000:
        str_out = 'one' + ' million'
    else:
        str_out = ''
    return str_out

def get_sum(int_limit):
    str_total = ''
    for i in range(1, int_limit+1):
        str_total += form_string(i)
    return len(str_total)

def main():
    int_test_val = int(input("Enter any value from 1 to 1,000,000: "))
    print("The sum of the string value of the numbers between 1 and " + str(int_test_val) + " is: " + str(get_sum(int_test_val)))


main()