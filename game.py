import random
choices=["rock","paper","scissor"]

user=input("enter thr choice:").lower()
computer=random.choice(choices)
print("computer choose:",computer)
if user==computer:
    print("tie")

elif(user=="rock" and computer=="scissor")or\
    (user=="paper" and computer=="rock")or\
    (user=="scissor" and computer=="paper"):
    print("you win")
else: 
    print("computer wins")
