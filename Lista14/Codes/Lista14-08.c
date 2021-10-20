#include <stdio.h>
#include <stdlib.h>

int quotient(int x, int y)
{
    if (y == 0)
    {
        return -1;
    }

    if (x < y)
    {
        return 0;
    }

    if (x == y)
    {
        return 1;
    }

    return (1 + quotient((x - y), y));
}

int main()
{
    int x, y;
    printf("Type the x value:");
    scanf("%d", &x);
    printf("Type the y value:");
    scanf("%d", &y);

    printf("The quotient is = %d\n", quotient(x, y));
    system("PAUSE");
    return 0;
}