binary_number = [1, 0, 1, 1, 1, 0, 1,1,1]
lenght = len(binary_number)
index = lenght-1
a = 1
sum = 0
while index >= 0:
    element = binary_number[index]
    binary = element*a
    sum = sum + binary
    index = index - 1
    a = a * 2
print(sum)
