#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 10;
    int v[n], inv[n];

    for (int i = 0; i < n; i++)
    {
        printf("%d° position:", i);
        scanf("%d", &v[i]);
        inv[n - i - 1] = v[i];
    }

    for (int i = 0; i < n; i++)
    {
        printf("\nReversed vector %d° pos = %d\n", i, inv[i]);
    }

    system("PAUSE");
    return 0;
}