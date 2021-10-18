#include <stdio.h>
#include <stdlib.h>

int calculateMOD(int x, int y)
{
    if (y == 0)
    {
        return -1;
    }

    if (x < y)
    {
        return abs(x);
    }

    if (x == y)
    {
        return 0;
    }

    return calculateMOD(abs(x - y), abs(y));
}

int main()
{
    int x, y;
    printf("Type the x value:");
    scanf("%d", &x);
    printf("Type the y value:");
    scanf("%d", &y);

    printf("The MOD is = %d\n", calculateMOD(x, y));
    system("PAUSE");
    return 0;
}
