#include<stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main(void){
    int test_cases;
    scanf("%d",&test_cases);
    while(test_cases > 0){
        int a, b;
        scanf("%d",&a);
        scanf("%d",&b);
        int apartment[a+1][b+1];
        for(int i = 0; i <= a; i++) {
            for(int j = 1; j <= b; j++) {
                if(i == 0) {
                    apartment[i][j] = j;
                }
                else {
                    int sum = 0;
                    for(int k = 1; k <= j; k++) {
                        sum += apartment[i-1][k];
                    }
                    apartment[i][j] = sum;
                }
            }
        }
        printf("%d\n", apartment[a][b]);
        test_cases--;
    }
    return 0;
}