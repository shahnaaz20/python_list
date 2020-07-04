question_list = [
	"Who is the first Indian woman wrestler to win a gold medal at the Asian Games?",
	"Which of these planets has a solid surface? ",
	"Which blood Group is universal donor? ",
    "from where does the veeru propose the basanti in sholay",
    "In the game of ludo the discs or tokens are of how many colours?"
]
options_list = [
	[" sakshi malik "," babita kumari "," vinesh phogat"," kavita devi"],
	[" saturn ", " jupiter ", " uranus ", " mars "],
	[" O +VE ", " O -VE ", " AB +VE ", " AB -VE "],
    [" Top of the roof"," Top of the hill"," Top of the water tank"," Top of the building"],
    [" one", " three"," four"," five"]
]
life_line = [[" sakshi malik "," vinesh phogat "],[" saturn "," mars "],
[" O -VE "," AB -VE"],[" Top of the hill"," Top of the water tank"],[" four"," five"]
]
answer_list = [3,4,2,3,3]
answer_life_line = [2,2,1,2,1]
index = 0
main_count = 1
option = 0
ans = 0
number = 1
amount = 0
print("        -:WELCOME TO KBC:-         ")
while index < len(question_list):
    print(str(main_count)+")"+str(question_list[index]))
    index_2 = 0
    count = 1
    while index_2 < len(options_list[index]):
        print(str(count)+"."+str(options_list[index][index_2]))
        count = count + 1
        index_2 = index_2 + 1
    guess = int(input(" Select a option Or You want to use life_line 5050:"))
    if guess == 5050:
      if number == 1:
       counter = main_count - 1
       print(" ")
       print(" Select one out of this two")
       while counter < len(life_line): 
        iterate = 0
        num = 1
        while iterate < len(life_line[iterate]):
            print(str(num)+"."+str(life_line[counter][iterate]))
            iterate = iterate + 1
            num = num + 1
        number = number + 1
        counter = counter + 1
        break
      else:
            print(" Sorry you have already used 5050")
      guess2 = int(input("Select your option once more: "))
      if guess2 == answer_life_line[ans] or guess2 == answer_list[option]:
        print(" Great! your answer is correct")
      else:
        print(" Sorry your answer is wrong,You are out of the game")
        break
    elif guess == answer_list[option]:
        print(" Great! your answer is correct")
    else:
        print(" Sorry your answer is wrong,You are out of the game ")
        break
    print(" ")
    main_count = main_count + 1
    index = index + 1
    amount = amount + 1000
    option = option + 1
    ans = ans + 1
print("your total amount is = " + str(amount))
print("       .........FINISH..........       ")     
