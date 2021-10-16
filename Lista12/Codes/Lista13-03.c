#include <stdio.h>
#include <stdlib.h>

int isPrime(int n)
{
    int isPrime = 1;

    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            isPrime = 0;
        }
    }

    return isPrime;
}

int main()
{
    int n = 0;

    printf("Type an integer:");
    scanf("%d", &n);

    if (isPrime(n))
    {
        printf("The number '%d' is prime.\n", n);
    }
    else
    {
        printf("The number '%d' is not prime.\n", n);
    }

    system("PAUSE");
    return 0;
}