/* Project Euler Problem 10 Expanded
 * This program will find the sum of all primes lower than a value N. N is 2,000,000 by default or can be passed
 * as a command line argument by the user.
 * By Kevin Moore
 */

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

bool isPrime(int iTestVal){
    bool bOut = true;
    int i;

    if (iTestVal < 2)
        bOut = false;
    else {
        for (i = 2; i <= sqrt(iTestVal); i++) {
            if (iTestVal % i == 0) {
                bOut = false;
                break;
            }
        }
    }
    return bOut;
}

unsigned long sumPrimesUnderN(int iLimit){
    unsigned long ulPrimeSum = 0;
    int i;
    for(i = 0; i < iLimit; i++){
        if (isPrime(i))
            ulPrimeSum += i;
    }
    return  ulPrimeSum;
}

int main(int argc, char* argv[]){
    int iLimit;
    // Check for user inputs
    switch(argc){
        case 1:
            iLimit = 2000000;
            printf("Running in standard mode with N value of %d\n", iLimit);
            break;
        case 2:
            iLimit = atoi(argv[1]);
            printf("Running in user defined mode with N value of %d\n", iLimit);
            break;
        default:
            iLimit = 2000000;
            printf("Invalid inputs, you may run with at most 1 integer values as arguments\n");
            printf("Running in standard mode with N value of %d\n", iLimit);
    }

    unsigned long ulOut = sumPrimesUnderN(iLimit);
    printf("The sum of all primes under %d is %lu\n", iLimit, ulOut);
}