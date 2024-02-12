#include <stdio.h>
#define MAX 50
#define r 31
#define M 1234567891

int main(void) {
    int a;
    char b[MAX];
    long long H = 0, R = 1;
    scanf("%d", &a);
    scanf("%s", b);
    for(int i = 0; i < a; i++){
        H = (H + (b[i] - 'a' + 1) * R) % M;
        R = (R * r) % M;
    }
    printf("%lld\n", H);
    return 0;
}
