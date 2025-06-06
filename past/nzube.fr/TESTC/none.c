#include <stdio.h>

char *check(char *dest)
{
        char xed[14] = "aeiouAEIOU";
        int y, i, t;
	char *text = " ";
        for (i = 0; xed[i] != '\0'; i++)
        {
                for (y = 0; dest[y] != '\0'; y++)
                {
                        if (dest[y] == xed[i])
			{
				int t = 0;
                                while (true)
                		{
					text[t] = dest[y];
					t++;
				}
			}
                }
        }
	text[t] = '\0';
	return (text);
}
