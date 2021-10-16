#include <stdio.h>
#include <stdlib.h>

double fahrToCels(double f)
{
    return ((f - 32) * 5) / 9;
}

double fahrToKel(double f)
{
    return (((f - 32) * 5) / 9) + 273.15;
}

double celsToFahr(double c)
{
    return ((c * 9) / 5) + 32;
}

double celsToKel(double c)
{
    return c + 273.15;
}

double kelToFahr(double k)
{
    return (((k - 273.15) * 9) / 5) + 32;
}

double kelToCels(double k)
{
    return k - 273.15;
}

int main()
{
    double v = 32.00;

    printf("F -> C = %.2lfC", fahrToCels(v));
    printf("\nF -> K = %.2lfK", fahrToKel(v));
    printf("\nC -> F = %.2lfF", celsToFahr(v));
    printf("\nC -> K = %.2lfK", celsToKel(v));
    printf("\nK -> F = %.2lfF", kelToFahr(v));
    printf("\nK -> C = %.2lfC\n", kelToCels(v));

    system("PAUSE");
    return 0;
}