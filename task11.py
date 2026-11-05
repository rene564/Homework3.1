best = -1
x = int(input())
while x != -1:
    if x > best:
        best = x
    x = int(input())
print(best)