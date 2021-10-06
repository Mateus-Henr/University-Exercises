#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 0;
    long sum = 0;

    printf("Vector's size:");
    scanf("%d", &n);

    int v[n];

    for (int i = 0; i < n; i++)
    {
        printf("%d° position:", i);
        scanf("%d", &v[i]);

        if (i % 2 == 0)
        {
            sum += v[i];
        }
    }

    printf("Sum = %ld\n", sum);
    system("PAUSE");
    return 0;
}
