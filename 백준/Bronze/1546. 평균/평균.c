#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
    int n;
    scanf("%d", &n);
    
    double scores[n];
    double max_score = 0;
    double sum = 0;
    
    for (int i = 0; i < n; i++) {
        scanf("%lf", &scores[i]);
        if (scores[i] > max_score) {
            max_score = scores[i];
        }
    }
    
    for (int i = 0; i < n; i++) {
        scores[i] = scores[i] / max_score * 100;
        sum += scores[i];
    }
    
    printf("%.2lf\n", sum / n);
    
    return 0;
}
