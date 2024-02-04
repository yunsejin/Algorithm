#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void) {
    int N;
    scanf("%d", &N);
    printf("int a;\n");
    printf("int *ptr = &a;\n");
    if (N > 1){
        printf("int **ptr2 = &ptr;\n"); 
    }
    for(int i = 3; i <= N; i++) {
        printf("int ");
        for(int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("ptr%d = &ptr%d;\n", i, i - 1);
    }
}