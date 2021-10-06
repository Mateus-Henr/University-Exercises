#include <stdio.h>
#include <stdlib.h>

int main()
{
    long sum = 0;

    while (1)
    {
        int n = 0;
        printf("Number:");
        scanf("%d", &n);

        if (n == -1)
        {
            break;
        }

        if (n < 0)
        {
            continue;
        }

        sum = sum + n;
    }

    printf("Total = %ld\n", sum);
    system("PAUSE");
    return 0;
}