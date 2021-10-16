#include <stdio.h>
#include <stdlib.h>

int main()
{
    int count = 1;
    long sum = 0;

    for (int i = 38; i > 1; i--)
    {
        printf("%d * %d / %d %s ", i - 1, i, count, i != 2 ? "+" : "");
        sum += ((i - 1) * i) / count;
        count++;
    }

    printf("\nSum = %ld\n", sum);
    system("PAUSE");
    return 0;
}