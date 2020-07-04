num = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index = 0
sum=0
count_1 = 0
count_2 = 0
sum_1=0
sum_2=0 
while index < len(num):
    if num[index]%2 != 0:
        sum_1 = sum_1+num[index]
        count_1 = count_1 + 1
    else:
        sum_2=sum_2+num[index]
        count_2 = count_2 + 1
    sum=sum+num[index]
    index = index + 1
print("count of odd = "+str(count_1))
print("count of even = "+str(count_2))
print("count of all number =  "+str(len(num)))
print("sum of odd numbers = "+str(sum_1))
print("sum of even numbers = "+str(sum_2))
print("sum of all numbers = "+str(sum))
print("avarage of odd numbers = "+str(sum_1/count_1))
print("average of even number = "+str(sum_2/count_2))
print("avarege of sum = "+str(sum/len(num)))