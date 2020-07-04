num = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index = 0
count_1=0
count_2=0
while index < len(num):
    if num[index]%2 != 0:
        # ("odd: " + str(num[index]))
        count_1=count_1+1
    else:
        # print("even: " + str(num[index]))
        count_2=count_2+1
    index = index + 1
print ("odd numbers of people",count_1)
print ("even numbers of people",count_2)