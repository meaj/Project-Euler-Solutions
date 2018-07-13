# This program will find all multiples of five and three below 1000
# 
# By Kevin Moore

def main():
    sums = 0
    for i in range(0,1000):
        if i % 3 == 0 and i % 5 == 0:
            sums -= i
		if i % 3 == 0 or i % 5 == 0:
			sums += i
    print(sums)
	ex = input("Press any key to exit.")
	print(ex)

main()
