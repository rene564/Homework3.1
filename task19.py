n = int(input())
total = 0
for a in range(n + 1):
    for b in range(a, n + 1):
        total += a + b
print(total)