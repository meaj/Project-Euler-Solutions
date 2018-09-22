/* Project Euler Problem 10
 * This program will find the sum of all primes lower than 2000000
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
    unsigned long ulOut = sumPrimesUnderN(2000000);
    printf("The sum of all primes under 2000000 is %lu\n", ulOut);
}