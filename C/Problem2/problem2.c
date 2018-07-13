/* Project Euler Problem 2
 * 		A modified solution to problem 2 from projecteuler.net
 * 		By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>

#define MAX_VAL 4000000

int main(int argc, char * argv[]){
	// Three values, previous fibonacci number, current fibonacci number, and sum
	unsigned long int lst = 1, cur = 2, tmp = 0, sum = 0;
	
	while (lst < MAX_VAL){
		tmp = cur; // store current value
		cur = lst + tmp; // add previous value to current value
		lst = tmp; // reassign previous value
		// if previous value is even, add to our sum
		if (lst % 2 == 0){
			sum += lst;
		}
	}
	
	printf("The sum of the even fibonacci numbers less than 4 million is: %lu\n", sum);
	
	return 0;
}