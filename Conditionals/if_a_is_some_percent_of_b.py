a = [160,140,155,190,162]
b = [60,100,69,84,151]

percentage = 0.95

c = []

for i in range(len(a)):
    if b[i] < percentage*a[i]:
        c.append(True)
    else:
        c.append(False)

print(c)