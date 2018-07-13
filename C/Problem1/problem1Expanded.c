/* Project Euler Problem 1 Expanded
 * 		A modified solution to problem 1 from projecteuler.net
 *		Allows for variable division checks and or variable range
 * 		By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
	int i = 0, lo_div = 0 , hi_div = 0, max = 0;
	unsigned long int sum = 0;
	// If no input is provided, the program runs in standard mode, with divisors 3 and 5, and range 1000
	if (argc == 1){
		printf("Running in standard mode:\n\n");
		max = 1000;
		lo_div = 3;
		hi_div = 5;
	}
	// If one input is provided, variable range mode is activated, where the max is set by the user
	if (argc == 2){
		printf("Running in variable range mode:\n\n");
		max = atoi(argv[1]);
		lo_div = 3;
		hi_div = 5;
	}
	// If two inputs are provided, user defined divisors are used
	// Allows divisors to be entered in any order
	if (argc == 3){
		max = 1000;
		lo_div = atoi(argv[1]);
		hi_div = atoi(argv[2]);
		if (lo_div > hi_div){
			int t;
			t = hi_div;
			hi_div = lo_div;
			lo_div = t;
		}
	}
	// If 3 inputs are provided, user defined divisors and range are used
	// Assumes range is always provided last
	if (argc == 4){
		lo_div = atoi(argv[1]);
		hi_div = atoi(argv[2]);
		max = atoi(argv[3]);
		if (lo_div > hi_div){
			int t;
			t = hi_div;
			hi_div = lo_div;
			lo_div = t;
		}
	}
	
	// Runs the loop from the lowest of the two divisors to max
	for (i = lo_div; i < max; i++){
		// If the number is divisible by both divisors we don't want to double count
		if (i % lo_div == 0 && i % hi_div == 0){
			sum += i;
		}
		else if (i % lo_div == 0){
			sum += i;
		}
		else if (i % hi_div == 0){
			sum += i;
		}
	}
	
	printf("The sum of all the multiples of %d or %d below %d is: %lu\n",lo_div, hi_div, max, sum);
	return 0;
}