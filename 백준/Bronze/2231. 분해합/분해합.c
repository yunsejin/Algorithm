#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main()
{
    int n;
    scanf("%d", &n);
    int i = 1;
    int sum;
    while (i <= n)
    {
        int a = i;
        sum = i;
        while(a > 0)
        {
            sum = sum + a % 10;
            a = a / 10;
        }
        if (sum == n)
        {
            printf("%d", i);
            break;
        }
        if (i == n)
        {
            printf("0");
            break;
        }
        i++;
    }
}