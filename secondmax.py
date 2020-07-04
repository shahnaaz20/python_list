
list = [2,378,568,77,5]
i = 0
max2 = 0
max = 0
while i < len(list):
    if list[i]>max:
        max2=max
        max=list[i]
    elif list[i]>max2 and max!=list[i]:
        max2=list[i]
    else:
        if max2==max:
            max2=list[i]
    i = i + 1
print(max2)