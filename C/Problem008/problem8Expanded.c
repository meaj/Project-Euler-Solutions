/* Project Euler Problem 8 Expanded
 * This program will find the largest product of N consecutive digits in a 1000 digit number
 * The value N can be provided by the user or will default to 13
 * By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char sNumber[] = "73167176531330624919225119674426574742355349194934"
                 "96983520312774506326239578318016984801869478851843"
                 "85861560789112949495459501737958331952853208805511"
                 "12540698747158523863050715693290963295227443043557"
                 "66896648950445244523161731856403098711121722383113"
                 "62229893423380308135336276614282806444486645238749"
                 "30358907296290491560440772390713810515859307960866"
                 "70172427121883998797908792274921901699720888093776"
                 "65727333001053367881220235421809751254540594752243"
                 "52584907711670556013604839586446706324415722155397"
                 "53697817977846174064955149290862569321978468622482"
                 "83972241375657056057490261407972968652414535100474"
                 "82166370484403199890008895243450658541227588666881"
                 "16427171479924442928230863465674813919123162824586"
                 "17866458359124566529476545682848912883142607690042"
                 "24219022671055626321111109370544217506941658960408"
                 "07198403850962455444362981230987879927244284909188"
                 "84580156166097919133875499200524063689912560717606"
                 "05886116467109405077541002256983155200055935729725"
                 "71636269561882670428252483600823257530420752963450";

unsigned long calculateProduct(int iStart, int iRange){
    unsigned long ulProduct = 1;
    int i;
    // Calculate product
    for (i = 0; i < iRange; i++){
        ulProduct *= (sNumber[iStart + i] - '0');
    }
    return ulProduct;
}

unsigned long findLargestProduct(int iRange){
    // Declare counters, length, and product holders
    unsigned long ulMaxProduct = 0, ulProduct;
    int iLen = sizeof(sNumber);
    int i, j;

    // Cycle through each 13 character iteration
    for (i = 0; i < iLen - iRange; i++){
        // Find the product of the current substring
        ulProduct = calculateProduct(i, iRange);

        if (ulProduct > ulMaxProduct)
            ulMaxProduct = ulProduct;
    }
    return ulMaxProduct;
}

int main(int argc, char * argv[]){
    int iValN;
    // Check for user input
    switch(argc){
        case 1:
            printf("Running in standard mode with N value of 13\n");
            iValN = 13;
            break;
        case 2:
            iValN = atoi(argv[1]);
            printf("Running in user defined mode with N value of %d\n", iValN);
            break;
        default:
            printf("Invalid inputs, you may run with at most 1 integer values as arguments\n");
            printf("Running in standard mode with N value of 13\n");
            iValN = 13;
    }

    unsigned long ulOut = findLargestProduct(iValN);
    printf("The largest product of %d consecutive digits in the given number is: %lu\n", iValN, ulOut);
}