/* Project Euler Problem 7
 * This program will find the 10,001st prime
 * By Kevin Moore
 */

#include <stdbool.h>
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

int generatePrimeN(int iNumPrime){
    int iPrimeCount = 0, iTest = 1;

    while (iPrimeCount < iNumPrime){
        if (isPrime(iTest))
            iPrimeCount++;
        iTest++;
    }

    return iTest-1;
}

int main(int argc, char * argv[]){
    int iVal = generatePrimeN(10001);
    printf("The 10001st prime number is: %d\n", iVal);
}