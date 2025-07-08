# SNAKE WATER GUN GAME
import random
'''
1 for Snake
-1 for Water
0 for Gun
'''

Computer = random.choice([-1,0,1])
you_str = input("Enter your choice : ")
you_dict = {"s":1,"w":-1,"g":0}
reverse_dict = {1:"Snake",-1:"Water",0:"Gun"}

you = you_dict[you_str]

print(f"You Chose {reverse_dict[you]}\nComputer Chose {reverse_dict[Computer]}")

if(Computer == you):
    print("Its a Draw")
else:
    if(Computer==-1 and you==1):
        print("You Win!!!")    
    elif(Computer==-1 and you==0):
        print("You Lose!!!") 
    elif(Computer==1 and you==-1):
        print("You Lose!!!") 
    elif(Computer==1 and you==0):
        print("You Win!!!") 
    elif(Computer==0 and you==-1):
        print("You Win!!!")
    elif(Computer==0 and you==1):
        print("You Lose!!!")             
    else:
        print("Something Went Wrong!!!")                     
