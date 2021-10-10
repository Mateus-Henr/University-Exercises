#include <stdio.h>
#include <stdlib.h>

int sumGrades(double *grades)
{
    double sum = 0.0;

    for (int j = 0; j < 5; j++)
    {
        sum += grades[j];
    }

    return sum >= 60 ? 1 : 0;
}

int main()
{
    double grades[10][5];

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf("%d l | %d col:", i, j);
            scanf("%lf", &grades[i][j]);
        }

        if (sumGrades(grades[i]))
        {
            printf("\nThe student %d has been approved.", i + 1);
        }
        else
        {
            printf("\nThe student %d has failed.", i + 1);
        }
    }

    system("PAUSE");
    return 0;
}