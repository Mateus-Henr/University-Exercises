#include <stdio.h>
#include <stdlib.h>

void printTable(int currIndex, int finalNum)
{
    if (currIndex > finalNum)
    {
        return;
    }

    printf("%d * %d = %d\n", currIndex, finalNum, (finalNum * currIndex));
    printTable((currIndex + 1), finalNum);
}

int main()
{
    int num;
    printf("Type the number:");
    scanf("%d", &num);

    printTable(1, num);
    system("PAUSE");
    return 0;
}