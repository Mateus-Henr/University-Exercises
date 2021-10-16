#include <stdio.h>
#include <stdlib.h>

double smallestNumber(double n1, double n2, double n3)
{
    double smallest = n1;
    smallest = n2 < n1 ? n2 : n1;
    smallest = n3 < smallest ? n3 : smallest;

    return smallest;
}

int main()
{
    double n1 = 0.0, n2 = 0.0, n3 = 0.0;

    printf("Numbers:");
    scanf("%lf %lf %lf", &n1, &n2, &n3);

    printf("The smallest number is %lf.\n", smallestNumber(n1, n2, n3));
    system("PAUSE");
    return 0;
}