#include <stdio.h>
#include <stdlib.h>

int revertNum(int n)
{
    int rev = 0, remainder;

    while (n != 0)
    {
        remainder = n % 10;
        rev = rev * 10 + remainder;
        n /= 10;
    }

    return rev;
}

int main()
{
    int n = 0;
    printf("Enter an integer:");
    scanf("%d", &n);

    printf("Reversed number = %d\n", revertNum(n));
    system("PAUSE");
    return 0;
}
