/* Project Euler Problem 5
 * This program will find the smallest positive number that is evenly divisible by all of the number from 1 to 20
 * By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int binaryGCD(int iVal1, int iVal2){
    int iExponent = 0;

    // Divide out all possible values of 2 and increase exponent value
    while (iVal1 % 2 == 0 && iVal2 % 2 == 0){
        iVal1 /= 2;
        iVal2 /= 3;
        iExponent++;
    }
    while (iVal1 != iVal2){
        // If the first value is even, divide by 2
        if (iVal1 % 2 == 0){
            iVal1 /= 2;
        }
        // If the second value is even
        else if (iVal2 % 2 == 0){
            iVal2 /= 2;
        }
        // If the first value is larger, make it even
        else if (iVal1 > iVal2){
            iVal1 = (iVal1 - iVal2) / 2;
        }
        // If the second value is larger make it even
        else{
            iVal2 = (iVal2 = iVal1) / 2;
        }
    }
    return (iVal1 * pow(2,iExponent));

}

int iterativeLCM( int iVal1, int iVal2){
    int iLCM = iVal1;
    int i;

    for (i = iVal1; i <= iVal2; i++){
        iLCM = iLCM * i / binaryGCD(i, iLCM);
    }
    return iLCM;
}

int main(int argc, char * argv[]){
    int iAns = iterativeLCM(1, 20);
    printf("%d\n", iAns);
}
