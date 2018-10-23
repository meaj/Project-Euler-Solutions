
# return the sum of the proper divisors of the passed in value int_val
def sum_proper_divisors( int_val ):
	int_sum = 0
	for i in range(1, int_val):
		if (int_val % i == 0):
			int_sum += i
	return int_sum
	
# Generates the sum of the amicable numbers under the limit int_limit	
def generate_sum_amicable_numbers_under_limit( int_limit ):
	int_sum = 0
	for int_lo in range(1, int_limit):
		int_hi = sum_proper_divisors(int_lo)
		if ( int_lo == sum_proper_divisors(int_hi) ) & ( int_hi > int_lo ):
			int_sum += int_lo + int_hi
	return sum
	

# Main driver function
def main():
	int_out = generate_sum_amicable_numbers_under_limit(10000)
	print("The sum of all the amicable numbers under 10,000 is " + str(int_out))

	
main()