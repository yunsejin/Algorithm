#include <stdio.h>

int n;
int stack[100000];
int top = -1;

void push(int x) {
    stack[++top] = x;
}

int pop() {
    return stack[top--];
}

int peek() {
    return stack[top];
}

int main() {
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        int h;
        scanf("%d", &h);

        while(top != -1 && peek() <= h) {
            pop();
        }
        push(h);
    }
    printf("%d\n", top+1);

    return 0;
}