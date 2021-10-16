#include <stdio.h>

int isInArray(char * a, int sizeArray, int v)
{
    int i = 0;

    for (i = 0; i < sizeArray; i++)
    {
        if (a[i] == (v + '0'))
        {
            return 1;
        }
    }

    return 0;
}

int main()
{
    int n = 0, i = 0, num = 0;
    scanf("%d", &n);

    int sizeArray = (n - 1) * 2;
    char s[sizeArray];
    scanf("%s %s", s, s);

    for (i = 1; i <= n; i++)
    {
        if (!isInArray(s, sizeArray, i))
        {
            num = i;
            break;
        }
    }

    printf("%d\n", num);
    return 0;
}