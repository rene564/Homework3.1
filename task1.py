count = 0
for n in range(100, 1000):
    if n % 17 == 0:
        print(n, end=" ")
        count+=1
print()
print(count)