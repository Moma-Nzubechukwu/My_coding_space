#include <stdio.h>

int main(void)
{
	int a, b, result;
	char c;
	printf("enter a number\n: ");
	scanf("%i", &a);
	printf("chose between'+','/', '-' or '*' :\n: ");
	scanf(" %c", &c);
	printf("enter another number:\n: ");
	scanf("%i", &b);

	if (c == '+')
		result = a + b;
	else if (c == '*')
                result = a * b;
	else if (c == '-')
                result = a - b;
	else if (c == '/')
                result = a / b;
	else
	{
		printf("incorret value\n");
		result = 0;
	}
	printf("result = %i\n", result);
	return 0;
}
