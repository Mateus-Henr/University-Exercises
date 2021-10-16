#include <stdio.h>
#include <stdlib.h>

void sortNumbersOut(int * v)
{
    int bool = 1;
    while (bool)
    {
        bool = 0;
        for (int i = 0; i < 10; i++)
        {
            if (v[i] > v[i + 1])
            {
                int temp = v[i];
                v[i] = v[i + 1];
                v[i + 1] = temp;
                bool = 1;
            }
        }
    }
}

int main()
{
    int v[10];

    for (int i = 0; i < 10; i++)
    {
        printf("Type the %d° number:", i + 1);
        scanf("%d", &v[i]);
    }

    sortNumbersOut(v);

    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", v[i]);
    }

    system("PAUSE");
    return 0;
}