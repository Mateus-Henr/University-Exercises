#include <stdio.h>
#include <stdlib.h>

int posOrNeg(int n)
{
    return (n > 0) ? 1 : 0;
}

int main()
{
    int n = 0;

    printf("Number:");
    scanf("%d", &n);

    if (n == 0)
    {
        printf("The number is zero.\n");
    }
    else if (posOrNeg(n))
    {
        printf("The number is positive.\n");
    }
    else
    {
        printf("The number is negative.\n");
    }

    system("PAUSE");
    return 0;
}