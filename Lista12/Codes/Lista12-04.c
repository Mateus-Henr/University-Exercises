#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int n = 0;

    printf("Type the number:");
    scanf("%d", &n);

    if (n >= 0)
    {
        printf("Square root = %lf", sqrt(n));
    }
    else
    {
        printf("Square = %d\n", n * n);
    }

    system("PAUSE");
    return 0;
}