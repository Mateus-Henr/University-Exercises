#include <stdio.h>
#include <stdlib.h>

double calcArithAvg(double g1, double g2, double g3)
{
    return (g1 + g2 + g3) / 3;
}

int main()
{
    int g1 = 0, g2 = 0, g3 = 0;

    printf("Type the three grades:");
    scanf("%d %d %d", &g1, &g2, &g3);

    printf("The arithmetic avg is %.2lf\n", calcArithAvg(g1, g2, g3));
    system("PAUSE");
    return 0;
}