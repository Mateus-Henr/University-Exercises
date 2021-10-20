#include <stdio.h>
#include <stdlib.h>

void createLine(unsigned int currElem)
{
    if (currElem == 0)
    {
        return;
    }

    printf("* ");
    createLine((currElem - 1));
}

void createSquare(unsigned int finalNum, unsigned int currLine)
{
    if (currLine == 0)
    {
        return;
    }

    createLine(finalNum);
    printf("\n");
    createSquare(finalNum, (currLine - 1));
}

int main()
{
    unsigned int n;
    printf("Type a number:");
    scanf("%d", &n);

    createSquare(n, n);
    system("PAUSE");
    return 0;
}
