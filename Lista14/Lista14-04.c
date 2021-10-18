#include <stdio.h>
#include <stdlib.h>

void printOddNumbers(int currNum, int end)
{
    if (currNum > end)
    {
        return;
    }

    printf("%d\n", currNum);
    printOddNumbers((((currNum % 2) == 0) ? (currNum + 1) : (currNum + 2)), end);
}

int main()
{
    printOddNumbers(0, 100);
    system("PAUSE");
    return 0;
}

