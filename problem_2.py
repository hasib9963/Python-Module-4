def good_sequence():
    N = int(input())
    a = list(map(int, input().split()))
    count = {}
    for num in a:
        if num not in count:
            count[num] = 0
        count[num] += 1
    result = 0
    for num, freq in count.items():
        if freq > num:
            result += freq - num
        elif freq < num:
            result += freq
    return result
print(good_sequence())
