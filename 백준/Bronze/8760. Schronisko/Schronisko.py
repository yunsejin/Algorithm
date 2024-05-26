def max_tourists(W, K):
    return (W * K) // 2

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    Z = int(data[0])
    results = []
    index = 1
    for _ in range(Z):
        W = int(data[index])
        K = int(data[index + 1])
        index += 2
        results.append(max_tourists(W, K))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
