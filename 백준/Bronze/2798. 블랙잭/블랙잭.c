#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
  int n, m;
  int o[100] = {0, };
  int sum, max = 0;
  scanf("%d %d",&n,&m);
  for (int i = 0; i < n; i++){
    scanf("%d", &o[i]);
  }
  for (int i = 0; i < n; i++){
    for (int j = i+1; j < n; j++){
      for (int k = j+1; k < n; k++){
          sum = o[i] + o[j] + o[k];
          if (sum > max && sum <= m){
            max = sum;
          }
      }
    }
  }
  printf("%d", max);
  return 0;
} 