#include <stdio.h>
#define MAX_HEAP_SIZE 100001

int min_heap[MAX_HEAP_SIZE] = {0};
int heap_size = 0;

void insert_heap(int val) {
    heap_size++;
    int current = heap_size;
    min_heap[current] = val;

    while (current > 1 && min_heap[current / 2] > min_heap[current]) {
        int temp = min_heap[current];
        min_heap[current] = min_heap[current / 2];
        min_heap[current / 2] = temp;
        current /= 2;
    }
}

int delete_min() {
    if (heap_size == 0) return 0;

    int min_val = min_heap[1];
    min_heap[1] = min_heap[heap_size];
    heap_size--;

    int current = 1;
    while (current * 2 <= heap_size) {
        int child = current * 2;
        if (child + 1 <= heap_size && min_heap[child + 1] < min_heap[child]) {
            child++;
        }
        if (min_heap[current] <= min_heap[child]) break;
        int temp = min_heap[current];
        min_heap[current] = min_heap[child];
        min_heap[child] = temp;
        current = child;
    }

    return min_val;
}

int main() {
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int temp;
        scanf("%d", &temp);
        if (temp == 0) {
            printf("%d\n", delete_min());
        } else {
            insert_heap(temp);
        }
    }

    return 0;
}