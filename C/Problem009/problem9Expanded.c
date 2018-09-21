/* Project Euler Problem 9
 * This program will find the pythagorean triplet for which a + b + c = 1000
 * By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Custom triplet structure containing three ints a, b, and c
typedef struct{
    int a;
    int b;
    int c;
} triplet;

// Finds the triplet such that a+b+c=N
triplet findTriplet(int iSumValue){
    int i;
    triplet ret;
    // iSumValue/3 is the limit because a<b<c
    for (i = 1; i < iSumValue/3; i++){
        ret.a = i;
        // b = (2aN - N^2)/(2(a - N))
        ret.b = (2*ret.a*iSumValue - pow(iSumValue,2))/(2 * (ret.a-iSumValue));
        //c = N - a - b
        ret.c = iSumValue - ret.a - ret.b;
        if((ret.a < ret.b < ret.c)&&(pow(ret.a,2) + pow(ret.b,2) == pow(ret.c,2)))
            return ret;

    }
    ret.a = ret.b = ret.c = -1;
    return ret;
}

int main(int argc, char * argv[]){
    int iDesiredSum;
    triplet out;

    // Check for user inputs
    switch(argc){
        case 1:
            iDesiredSum = 1000;
            printf("Running in standard mode with N value of %d\n", iDesiredSum);
            break;
        case 2:
            iDesiredSum = atoi(argv[1]);
            printf("Running in user defined mode with N value of %d\n", iDesiredSum);
            break;
        default:
            iDesiredSum = 1000;
            printf("Invalid inputs, you may run with at most 1 integer values as arguments\n");
            printf("Running in standard mode with N value of %d\n", iDesiredSum);
    }

    out = findTriplet(iDesiredSum);

    if (out.a + out.b + out.c != iDesiredSum){
        printf("There is no pythagorean triplet with sum a + b + c = %d\n", iDesiredSum);
    }
    else{
        printf("%d * %d * %d = %d\n", out.a, out.b, out.c, out.a * out.b * out.c);
    }
}