#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    int h, m;
    scanf("%d %d", &h, &m);
    if (m < 45) {
        if (h == 0) {
            h = 23;
        }
        else {
            h--;
        }
        m += 15;
    }
    else {
        m -= 45;
    }
    printf("%d %d", h, m);
    return 0;
}