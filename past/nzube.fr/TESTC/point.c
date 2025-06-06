#include <stdio.h>
#include <stdbool.h>
#include "none.c"
#include "check.c"
#include "main.h"
int check_vowel(char *dest);

int main(void)
{
	char str[14] = "aeiouAEIOU";
	char ter[98];
	printf("enter the word you want to check if it is  a vowel\n");

	scanf("%s", ter);
	char *male = check(ter);
        printf("%s", male);
	check_vowel(ter);
	


}
