#include <stdio.h>

int check_vowel(char *dest)
{
        char xed[14] = "aeiouAEIOU";
        int y, i;
        for (i = 0; xed[i] != '\0'; i++)
        {
                for (y = 0; dest[y] != '\0'; y++)
                {
                        if (dest[y] == xed[i])
                                printf("%c\n", dest[y]);
                }
        }
}
