magic = [
    [8, 3, 4],
    [1, 7, 7],
    [6, 7, 2]
]
i = 0
a=[]
while i < len(magic):
    j=0
    sum = 0
    while j < len(magic[i]):
        e = magic[i][j]
        sum= sum + e
        j = j + 1
    a.append(sum)
    print(sum)
    i = i + 1
print(a)
if a[0]==a[1] and a[0]==a[2]:
    if a[0]==a[1] and a[1]==a[2]:
        print("its a magic square")
else:
    print("not a magic square")