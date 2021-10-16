#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m[3][5], vectorSL[3];

    for (int i = 0; i < 3; i++)
    {
        int sum = 0;

        for (int j = 0; j < 5; j++)
        {
            printf("%d° line | %d col:", i, j);
            scanf("%d", &m[i][j]);
            sum += m[i][j];
        }
        vectorSL[i] = sum;
    }

    for (int i = 0; i < 3; i++)
    {
        printf("\nvectorSL %d° position = %d\n", i, vectorSL[i]);
    }

    system("PAUSE");
    return 0;
}

