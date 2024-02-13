#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
  int n, level = 1, room = 1;
  scanf("%d", &n);

  while (1) {
    if (n <= room) {
      break;
    }
    room += 6 * level;
    level++;
  }

  printf("%d\n", level);

  return 0;
}