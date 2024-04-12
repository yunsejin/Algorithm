import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    indexed_a = [(value, index) for index, value in enumerate(a)]
    indexed_a.sort()
    result = [0] * n
    current_compressed_value = 0
    result[indexed_a[0][1]] = current_compressed_value

    for i in range(1, n):
        if indexed_a[i][0] != indexed_a[i - 1][0]:
            current_compressed_value += 1
        result[indexed_a[i][1]] = current_compressed_value

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()