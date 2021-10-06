#include <stdio.h>
#include <stdlib.h>

int main()
{
    int grades[10][5];

    for (int i = 0; i < 10; i++)
    {
        double sum = 0;

        for (int j = 0; j < 10; j++)
        {
            printf("%d l | %d col:", i, j);
            scanf("%d", &grades[i][j]);
            sum += grades[i][j];
        }

        if (sum > 60)
        {
            printf("Student %d approved.\n", i);
        }
        else
        {
            printf("Student %d failed.\n", i);
        }
    }

    system("PAUSE");
    return 0;
}