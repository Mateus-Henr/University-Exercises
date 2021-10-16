#include <stdio.h>
#include <stdlib.h>

double mToFeet(double m)
{
    return (m * 39.37) / 12;
}

int main()
{
    double p = 0.0;
    printf("Meters:");
    scanf("%lf", &p);

    printf("It's %lf feet and inches.\n", mToFeet(p));
    system("PAUSE");
    return 0;
}