#include <stdio.h>
#include <stdlib.h>

int sumOfSquares(int *v)
{
    int sum = 0;

    for (int i = 0; i < 20; i++)
    {
        sum += (v[i] * v[i]);
    }

    return sum;
}

int main()
{
    int v[20];

    for (int i = 0; i < 20; i++)
    {
        printf("Type the %d° number:", i + 1);
        scanf("%d", &v[i]);
    }

    printf("Sum = %d\n", sumOfSquares(v));
    system("PAUSE");
    return 0;
}
