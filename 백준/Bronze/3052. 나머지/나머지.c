#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    int arr[10];
    int remain[42] = {0,};
    int count = 0;

    for(int i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
        remain[arr[i] % 42]++;
    }

    for(int i = 0; i < 42; i++) {
        if(remain[i] != 0) count++;
    }

    printf("%d", count);

    return 0;
}