import random

choice=('R','P','S')
def choice_list(player,computer):
   
        if (computer==player):
            return None
        if((player=='R' and computer=='S') or (player=='S' and computer=='P') or (player=='P' and computer=='R')):
            return True
        else:
            return False   

score=0
score1=0

def score_table():
    attempt=0
    while attempt<3:
            global score
            global score1
            pla=input("Enter your choice : ")
            player=pla.upper()
            computer=(random.randint(0,2))
            computer=choice[computer]
            win=choice_list(player,computer)
            print('Computer put ' , computer)
            if win is None:
                print("Match draws")
                attempt-=attempt
                
            elif win is True:
                print("You won")
                score=score+1
            
            else:
                print("You loses")
                score1+=1
            attempt+=1

    if score>score1:
    
        print('YOU WON THE MATCH ')
    elif score==score1:
        print('BOTH ARE WON')
    else:
        print('COMPUTER WON THE MATCH ')
score_table()

input1=input("Did you want to play again y/n?")

if(input1.lower()=="y"):
    score_table()
else:
    print("Thank you!!")
    
