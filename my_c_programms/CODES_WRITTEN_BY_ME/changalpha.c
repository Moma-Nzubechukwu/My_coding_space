#include <stdio.h>


int main()
{
	int a = 0;
	int b = 1;
	int limit = 0;
	int d, c;
	printf("enter the limit you want");
	scanf("%d", &limit);

	while( b <= limit)
	{
		c = a;
		d = b;
		a = b;
		b = c + d;
		if (b <= limit)
			printf("%i\n", b);
	}

	return (0);
}
