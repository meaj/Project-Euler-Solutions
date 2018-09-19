/* Project Euler Problem 6
 * This program will find the difference in the sum of the squares and the square of the sum of a range of integers
 * By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>

int calculateDifference( int iStop ){
    int iSquareSum = 0, iSumSquare = 0, i;

    iSquareSum = ((iStop *( iStop + 1 )) >> 1);
    iSquareSum *= iSquareSum;

    for(i = 1; i <= iStop; i++){
        iSumSquare += (i * i);
    }

    // printf("The square of the sum is: %d\n", iSquareSum);
    // printf("The sum of the squares is: %d\n", iSumSquare);

    return iSquareSum - iSumSquare;
}

int main(int argc, char * argv[]){
    int iOut = calculateDifference(100);
    printf("The difference between the sum of the squares and the square of the sum of the ");
    printf("natural numbers from 1 to 100 is %d\n", iOut);
}