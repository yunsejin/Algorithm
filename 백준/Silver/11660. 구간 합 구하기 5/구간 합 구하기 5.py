import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0

    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    matrix = []
    for i in range(N):
        row = list(map(int, data[idx:idx+N]))
        matrix.append(row)
        idx += N

    sum_matrix = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            sum_matrix[i][j] = matrix[i-1][j-1] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]

    results = []
    for _ in range(M):
        x1 = int(data[idx])
        idx += 1
        y1 = int(data[idx])
        idx += 1
        x2 = int(data[idx])
        idx += 1
        y2 = int(data[idx])
        idx += 1

        result = sum_matrix[x2][y2] - sum_matrix[x1-1][y2] - sum_matrix[x2][y1-1] + sum_matrix[x1-1][y1-1]
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
