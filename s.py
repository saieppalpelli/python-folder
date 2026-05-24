import random
num = random.randint(1,50)
print("guess the num(1 to 50)")
print("you have 3 chaances")
for i in range(3):
    guess=int(input("enter your guess:"))
    if guess==num:
        print("you win")
        break
    elif guess>num:
        print("too high")
    else:
        print("too low")
else:
        print("you lost")
        print("number was:",num)
