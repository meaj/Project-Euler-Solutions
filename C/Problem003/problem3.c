/* Project Euler Problem 3
 * 		A solution to problem 3 from projecteuler.net
 *		Includes variable run mode which allows the user to enter a different value to factor as argument
 * 		By Kevin Moore
 */
 
 #include <stdio.h>
 #include <stdlib.h>
 #include <math.h>
 
 // Test value provided by solution
 # define TST 13195
 // Test value used to ensure largestFactor() returns val if val is prime
 # define PRIME 13
 // Test value used to ensure largestFactor() is able to return 2 if applicable
 # define EVEN 4
 // Value required by problem
 # define MAX 600851475143
 
unsigned long int largestFactor(unsigned long int val){
	 int i = 0;
	 // The largest possible prime factor, will be less than the square root
	 int max = (int)sqrt((long double) val);
	 
	 // Factors out 2 until result is odd or 2 is reached
	 while (val % 2 == 0){
		 // When val is equal to 2, 2 is the largest prime factor
		 if (val == 2)
			 break;
		 val = val / 2;
		 //printf("%lu\n", val); // Test print, please ignore
	 }
	 
	 // Factors out all values between 3 and the maximum value
	 for(i = 3; i <= max; i += 2){
		 while(val % i == 0){
			 // When i = val we have found the larges prime factor and can stop searching, unless val is prime
			 if (i == val)
				 break;
			 val = val / i;
			 //printf("%lu\n", val); // Test print, please ignore
		 }
	 }
	 return val;
 }
 
 int main(int argc, char * argv[]){
	 unsigned long int val;
	 if (argc == 1){
		 val = MAX;
	 }
	 else if (argc == 2){
		 val = atoi(argv[1]);
	 }
	 
	 unsigned long int max_prime_factor = largestFactor(val);
	 printf("The maximum prime factor of %lu is %lu\n", val, max_prime_factor);
	 
 }