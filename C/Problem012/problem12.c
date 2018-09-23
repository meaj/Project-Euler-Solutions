/* Project Euler Problem 12
 * This program will find the first triangle number with over 500 divisors
 * By Kevin Moore
 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int calcNumberDivisors(unsigned long ulVal){
    int iNumDivisors = 0;
    unsigned long ulStop = (unsigned long)sqrt(ulVal);
    unsigned long i;

    printf("Testing number %lu\n", ulVal);

    for(i = 1; i <= ulStop; i++){
        if (ulVal % i == 0)
            iNumDivisors += 2;
        if (i == ulStop)
            iNumDivisors--;
    }

    printf("It has %d divisors\n", iNumDivisors);

    return iNumDivisors;
}

unsigned long genTriangleNumber(int iNumDivisors){
    int iCount = 0;
    unsigned long ulTriangleNumber;
    int iFoundDivisors = 0;
    while(iFoundDivisors < iNumDivisors){
        iCount++;
        ulTriangleNumber = (unsigned long)(iCount*(iCount+1))/2;
        iFoundDivisors = calcNumberDivisors(ulTriangleNumber);
    }
    return ulTriangleNumber;
}

int main(int argc, char * arcv[]){
    unsigned long ulOut = genTriangleNumber(500);
    printf("The first triangle number with 500 divisors is %lu\n", ulOut);
}