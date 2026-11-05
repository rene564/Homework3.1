x = int(input("Введите X: "))
for k in range(1, x + 1):
    total = 0
    line = ""
    for i in range(1, k + 1):
        total += i
        if i == 1:
            line += str(i)
        else:
            line += " + " + str(i)
    if k == 1:
        print(line)
    else:
        print(line, "=", total)