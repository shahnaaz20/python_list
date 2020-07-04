list1= [67,89,1,23,5,2]
i = 0
while i < len(list1):
    j =0
    while j < len(list1)-1:
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
        else:
            list1[j],list1[j+1]=list1[j],list1[j+1]
        j = j + 1
    i = i + 1
print(list1)
