def calculate_repayment(data_sets):
    results = []
    for i, data in enumerate(data_sets):
        n, s, d = data['info']
        total_value = 0
        
        for ship in data['ships']:
            distance, value = ship
            if distance / s <= d:
                total_value += value
        
        results.append(f"Data Set {i+1}:\n{total_value}\n")
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    K = int(data[0].strip())
    data_sets = []
    idx = 1
    
    for _ in range(K):
        n, s, d = map(int, data[idx].strip().split())
        idx += 1
        ships = []
        
        for _ in range(n):
            di, vi = map(int, data[idx].strip().split())
            ships.append((di, vi))
            idx += 1
        
        data_sets.append({'info': (n, s, d), 'ships': ships})
    
    results = calculate_repayment(data_sets)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
