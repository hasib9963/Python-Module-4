def max_operations(arr):
    count = 0
    while all(num % 2 == 0 for num in arr):
        arr = [num // 2 for num in arr]
        count += 1
    return count
N = int(input())
A = list(map(int, input().split()))
result = max_operations(A)
print(result)
