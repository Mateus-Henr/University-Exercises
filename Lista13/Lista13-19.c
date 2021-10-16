#include <stdio.h>
#include <stdlib.h>

int sum(int *v)
{
    int sum = 0;

    for (int i = 0; i < 15; i++)
    {
        sum += v[i];
    }

    return sum;
}

int main()
{
    int v[15];

    for (int i = 0; i < 15; i++)
    {
        printf("Type the %d° number:", i + 1);
        scanf("%d", &v[i]);
    }

    printf("Sum = %d\n", sum(v));
    system("PAUSE");
    return 0;
}
