/* Project Euler Problem 4
 * This program will find the largest palindrome formed by three digit numbers
 * By Kevin Moore
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define LENGTH(x) (sizeof(x)/sizeof(x[0]))

// Determines if the passed in integer is a palindrome or not
int isPalindrome(int iVal){
    int i, iLen;
    char str[6];
    int bRet = 1;

    // Convert integer to string
    sprintf(str, "%d", iVal);
    // Determine length of string
    iLen = LENGTH(str);
    // Loop through each char until the middle chars are reached or a mismatch found
    for (i = 0; i < iLen/2; i++) {
        if (str[i] != str[iLen-i-1]){
           bRet = 0;
           break;
        }
    }
    return  bRet;
}

// Gets the largest palindrome within a range of values
int getMaxPalindrome(int iStart, int iStop){
    int i, j, iTst;
    int iMax = 0;
    for (i = iStart; i < iStop; i++){
        for( j = iStart; j < iStop; j++) {
            iTst = i * j;
            if (isPalindrome(iTst)){
                if (iTst > iMax)
                    iMax = iTst;
            }
        }
    }
    return iMax;
}

int main(int argc, char * argv[]){
    int maxPalindrome = getMaxPalindrome(101,999);
    printf("%d\n", maxPalindrome);
}
