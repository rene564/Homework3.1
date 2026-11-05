n, k, r = map(int, input().split())
d = 1
while n < r:
    n += n * k / 100
    d += 1
print(d)