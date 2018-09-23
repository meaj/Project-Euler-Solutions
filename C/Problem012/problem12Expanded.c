/* Project Euler Problem 12 Expanded
 * This program will find the first triangle number with over N divisors
 * N is specified by the user or defaults to 500
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

int main(int argc, char * argv[]){
    int iNumDivisors;

    // Verifies user input
    switch(argc){
        case 1:
            iNumDivisors = 500;
            printf("Running in standard mode with N value of %d\n", iNumDivisors);
            break;
        case 2:
            iNumDivisors = atoi(argv[1]);
            if ((3 <= iNumDivisors)) {
                printf("Running in user defined mode with N value of %d\n", iNumDivisors);
                break;
            }
        default:
            iNumDivisors = 500;
            printf("Invalid inputs, you may run with at most 1 integer value greater than 2\n");
            printf("Running in standard mode with N value of %d\n", iNumDivisors);
    }

    unsigned long ulOut = genTriangleNumber(iNumDivisors);
    printf("The first triangle number with 500 divisors is %lu\n", ulOut);
}