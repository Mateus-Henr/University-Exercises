#include <stdio.h>
#include <stdlib.h>

int main()
{
    double facCost = 0, consCost = 0, percDis = 0.28, percTax = 0.45;

    printf("Type the factory cost: R$");
    scanf("%lf", &facCost);

    consCost = facCost + (facCost * percDis) + (facCost * percTax);
    printf("The consumer's cost is R$%.2lf\n", consCost);

    system("PAUSE");
    return 0;
}
