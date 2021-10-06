#include <stdio.h>
#include <stdlib.h>

int evenOrOdd(int n)
{
    return (n % 2 == 0) ? 0 : 1;
}

int main()
{
    int n = 0;

    printf("Type an integer:");
    scanf("%d", &n);

    if (evenOrOdd(n))
    {
        printf("The number '%d' is odd.\n", n);
    }
    else
    {
        printf("The number '%d' is even.\n", n);
    }

    system("PAUSE");
    return 0;
}