"""
This program recursively finds the longest Collatz sequence with a starting value less than 1000000
By Kevin Moore
"""

lst_chain = []

def collatz_recur(lst_chain):
	# Base case
	if (lst_chain[-1] == 1):
	    return lst_chain
	# Even recursive case
	if (lst_chain[-1] % 2 == 0):
	    lst_chain.append(lst_chain[-1]/2)
	    return collatz_recur(lst_chain)
	# Odd recursive case
	elif (lst_chain[-1] % 2 == 1):
	    lst_chain.append((lst_chain[-1]*3)+1)
	    return collatz_recur(lst_chain)

def million_search():
	int_max_len = 0
	lst_max_chain = []
	for i in range(1000000):
	    print("Testing value " + str(i))
	    lst_tmp = [i]
	    lst_tmp = collatz_recur(lst_tmp)
	    if lst_tst_chain.length() > int_max_len:
	        int_max_len = lst_tst_chain.length()
	        lst_max_chain = lst_tmp
	return lst_max_chain

def main():
	lst_chain = million_search()
	print(lst_chain[1])

main()