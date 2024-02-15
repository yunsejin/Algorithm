#include <stdio.h>
#include <string.h>

int isPalindrome(char *str) {
    int length = strlen(str);
    for (int i = 0; i < length / 2; i++) {
        if (str[i] != str[length - i - 1]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char num[6];
    while (1) {
        scanf("%s", num);

        if (strcmp(num, "0") == 0)
            break;

        if (isPalindrome(num))
            printf("yes\n");
        else
            printf("no\n");
    }

    return 0;
}