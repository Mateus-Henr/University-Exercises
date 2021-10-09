#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double calcDelta(double a, double b, double c)
{
    return (b * b) - (4 * a * c);
}

void calcRoots(double a, double b, double c)
{
    double delta = calcDelta(a, b, c);

    if (delta < 0)
    {
        printf("The equation can't be solved since delta is negative and negative numbers don't have square root.\n");
    }
    else
    {
        double x1 = (-b + sqrt(delta)) / (2 * a);
        double x2 = (-b - sqrt(delta)) / (2 * a);

        printf("The roots of the equation are x1 = %lf and x2 = %lf\n", x1, x2);
    }
}

int main()
{
    double a = 0, b = 0, c = 0;

    printf("Type the a, b and c:");
    scanf("%lf %lf %lf", &a, &b, &c);

    calcRoots(a, b, c);

    system("PAUSE");
    return 0;
}