#include <stdio.h>
#include <stdlib.h>

int isDivisibleByThree(int n)
{
    return (n / 3) ? 1 : 0;
}

int main()
{
    int v[5];

    for (int i = 0; i < 5; i++)
    {
        printf("Type the %d° number:", i + 1);
        scanf("%d", &v[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        if (isDivisibleByThree(v[i]))
        {
            printf("The number '%d' is divisible by three.", v[i]);
        }
        else
        {
            printf("The number '%d' is NOT divisible by three.", v[i]);
        }
    }

    system("PAUSE");
    return 0;
}