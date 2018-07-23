/* Project Euler Problem 1
 * 		A solution to problem 1 from projecteuler.net
 * 		By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
	int i = 0, sum = 0;
	
	for (i = 3; i < 1000; i++){
		// if the number is divisible by both 3 and 5 we don't want to double count
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
	
	printf("The sum of all the multiples of 3 or 5 below 1000 is: %d\n", sum);
	return 0;
}