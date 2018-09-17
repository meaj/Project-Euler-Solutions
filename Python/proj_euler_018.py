"""
This program finds the maximum path in a triangle of values
By Kevin Moore
"""

# Triangle of values to find the maximum path through
lst_triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

def find_path(lst_input):
    # Copy the input into an empty triangle that can store the maximum path of each sub triangle at given indices
    lst_paths = lst_input
    # Starting at the second from the bottom row, add up the maximum value of the lower neighbors of a given index
    for row in reversed(range(len(lst_input) - 1)):
        for col in range(len(lst_input[row])):
            lst_paths[row][col] += max(lst_input[row+1][col], lst_input[row+1][col+1])
        #print("The max paths of rows " + str(row) + " and " + str(row+1))
        #print(lst_paths[row])
    # After calculation, the maximum value will be at the top
    return lst_paths[0][0]

def main():
    print("The maximum path through the triangle is " + str(find_path(lst_triangle)))

main()