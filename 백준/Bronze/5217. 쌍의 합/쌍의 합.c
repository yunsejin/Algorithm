#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void)
{
    int a, b, c, d, i;
    scanf("%d", &a);
    for (i = 0; i < a; i++)
    {
        scanf("%d", &b);
        if (b == 2)
        {
            printf("Pairs for 2:\n");
        }
        else if (b == 3)
        {
            printf("Pairs for 3: 1 2\n");
        }
        else if (b == 4)
        {
            printf("Pairs for 4: 1 3\n");
        }
        else
        {
            printf("Pairs for %d: ", b);
            char str[256] = "";
            for (c = 1; c < b; c++)
            {
                for (d = c + 1; d < b; d++)
                {
                    if (c + d == b)
                    {
                        char tmp[32];
                        sprintf(tmp, "%d %d, ", c, d);
                        strcat(str, tmp);
                    }
                }
            }
            str[strlen(str)-2] = '\0';
            printf("%s\n", str);
        }
    }
}
