#include <stdio.h>
#include <stdlib.h>

unsigned int fb(unsigned int currTerm, unsigned int currValue, unsigned int lastValue)
{
    if (currTerm == 0)
    {
        return currValue;
    }

    if (currTerm == 1)
    {
        return lastValue;
    }

    return fb((currTerm - 1), lastValue, (lastValue + currValue));
}

int main()
{
    unsigned int term;
    printf("Inform the term that you'd like:");
    scanf("%d", &term);

    printf("%d", fb(term, 0, 1));

    printf("\nThe first 20 terms:\n");
    for (unsigned int i = 0; i < 20; i++)
    {
        printf("%d ", fb(i, 0, 1));
    }
    system("PAUSE");
    return 0;
}