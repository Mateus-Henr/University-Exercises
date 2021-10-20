#include <stdio.h>
#include <stdlib.h>

unsigned int factorial(unsigned int currTerm, unsigned int currValue)
{
    if (currValue < 0)
    {
        return -1;
    }

    if (currValue == 0)
    {
        return 1;
    }

    if (currTerm == 1)
    {
        return currValue;
    }

    return factorial((currTerm - 1), ((currTerm - 1) * currValue));
}

int main()
{
    int num;
    printf("Type the number:");
    scanf("%d", &num);

    printf("The factorial is = %d\n", factorial(num, num));
    system("PAUSE");
    return 0;
}