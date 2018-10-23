"""
This program finds the sum of all the numerical values of the characters of the names provided in the file names.txt
See https://projecteuler.net/problem=22 for a better explanation of what this does
By Kevin Moore
"""

import csv


# Convert ascii char to int value with a = A = 1
def ascii_to_int( char ):
    return ord(char.upper()) - 64


# Parses csv file	
def parse_file( str_filename ):
    lst_strings = []
    with open(str_filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter = ',')
        # This loop may be redundant as there should only be one row in the csv
        for row in readCSV:
            for entry in row:
                    lst_strings.append(entry)
    lst_strings.sort()
    csvfile.close()
    return lst_strings


# Calculates the scores for the entire list of names
def calculate_scores( list_strings ):
    int_multiplier =  0
    lst_scores = []
    for string in list_strings:
        int_multiplier += 1
        int_base = 0
        for char in string:
            int_base += ascii_to_int(char)
        lst_scores.append(int_base*int_multiplier)
    return lst_scores


# Main driver function
def main():
    strings = parse_file("Inputs/names.txt")
    out = sum(calculate_scores(strings))
    print("The sum of the name scores in the file is " + str(out))


main()