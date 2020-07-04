number = 30
n = [10, 11, 12, 22,13, 14,16, 17,8, 18, 19]
b = []
i = 1
index = len(n)-1
while i < len(n)/2:
    a = []
    if n[index]+n[i]==30:
        a.append(n[i])
        a.append(n[index])
        b.append(a)
    i = i + 1
    index = index - 1
print(b)
