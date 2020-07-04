marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
count=1
i = 0
n=0
while i <len(marks):
    n = 0 
    sum = 0
    while n < len(marks[i]):
        a = marks[i][n]
        sum = sum + a
        n = n + 1
    avarage = sum/len(marks[i])
    avarage_marks=(int(avarage))
    print ("avarage of",count,"year",avarage_marks)
    count=count+1
    i = i + 1