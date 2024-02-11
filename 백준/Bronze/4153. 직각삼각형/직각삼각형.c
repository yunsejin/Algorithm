#include <stdio.h>

int main(void) {
    int i,j,k;
    while(1){
        scanf("%d %d %d", &i, &j, &k);
        if (i==0 && j==0 && k==0) break;
        if(i*i + j*j == k*k || i*i + k*k == j*j || j*j + k*k == i*i)
            printf("right\n");
        else printf("wrong\n");
    }
    return 0;
}