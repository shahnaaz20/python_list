money = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
index = 0
crorepati = 0
lakhpati = 0
dilwale = 0
while index < len(money):
    if money[index] >= 10000000:
        crorepati = crorepati + 1
    elif money[index] >= 100000:
        lakhpati = lakhpati + 1
    else:
        dilwale = dilwale + 1
    index = index + 1
print(str(crorepati) +" "+"crore_pati hai")
print(str(lakhpati) +" "+"lakh_pati  hai")
print(str(dilwale) +" "+"dil_wale hai")