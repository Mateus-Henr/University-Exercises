#include <stdio.h>
#include <stdlib.h>

void multipleOfFive(int currNum, int end)
{
    if (currNum >= end)
    {
        return;
    }

    if ((currNum % 5) == 0)
    {
        printf("%d\n", currNum);
    }
    multipleOfFive((currNum + 1), end);
}

int main()
{
    int start, end;
    printf("Type the start number:");
    scanf("%d", &start);
    printf("Type the end number:");
    scanf("%d", &end);

    multipleOfFive(start, end);
    system("PAUSE");
    return 0;
}