#include <stdio.h>
#include <stdlib.h>

void printMDC(int x, int y)
{
    if (x == y)
    {
        printf("MDC(%d, %d) = %d\n", x, y, x);
        return;
    }

    printf("MDC(%d, %d) = ", x, y);
    if (x < y)
    {
        printMDC(y, x);
    }
    else
    {
        printMDC((x - y), y);
    }
}

int main()
{
    int x, y;
    printf("Type the x value:");
    scanf("%d", &x);
    printf("Type the y value:");
    scanf("%d", &y);

    printMDC(x, y);
    system("PAUSE");
    return 0;
}