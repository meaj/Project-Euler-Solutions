/* Project Euler Problem 1 Expanded
 * 		A modified solution to problem 1 from projecteuler.net
 *		Allows for variable division checks and or variable range
 * 		By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
	int max = 0;
	unsigned long int i = 0, sum = 0;
	// If no input is provided, the program runs in standard mode, with divisors 3 and 5, and range 1000
	if (argc == 1){
		printf("Running in standard mode:\n\n");
		max = 1000;
	}
	// If one input is provided, variable range mode is activated, where the max is set by the user
	if (argc == 2){
		printf("Running in variable range mode:\n\n");
		max = atoi(argv[1]);
	}
	
	// Runs the loop from the lowest of the two divisors to max
	for (i = 3; i < max; i++){
		// If the number is divisible by both divisors we don't want to double count
		if (i % 3 == 0 && i % 5 == 0){
			sum += i;
		}
		else if (i % 3 == 0){
			sum += i;
		}
		else if (i % 5 == 0){
			sum += i;
		}
	}
	
	printf("The sum of all the multiples of 3 or 5 below %d is: %lu\n", max, sum);
	
}