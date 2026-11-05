n = int(input())
for num in range(1, n + 1):
    total = 0
    for d in range(1, num // 2 + 1):
        if num % d == 0:
            total += d
    if total == num:
        print(num)