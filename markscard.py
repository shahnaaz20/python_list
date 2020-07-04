marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78]
]
sum = 0
i = 0
while i <len(marks):
    n = 0
    while n < len(marks[i]):
        a = marks[i][n]
        sum = sum + a
        n = n +1
    i = i + 1
print(sum)
