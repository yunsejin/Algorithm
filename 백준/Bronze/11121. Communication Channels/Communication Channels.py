def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        input_string, output_string = data[i].split()
        if input_string == output_string:
            results.append("OK")
        else:
            results.append("ERROR")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
