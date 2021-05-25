import random
import sys

maximum_value=30
dice=6

snake={29:5,26:13,23:10,20:2,8:1}
ladder={3:22,14:28,6:16,4:12,11:19}

print("-----WELCOME TO SNAKE AND LADDER GAME-----")
print("++++++++++   HAVE FUN   +++++++++++")
def player_names():
   
    player1_name = str(input("Enter player1 name: "))
    player2_name = str(input("Enter player2 name: "))
    print( "Player " + player1_name + "' and '" + player2_name + " are playing \n")

    return player1_name, player2_name

def dice_value():
  
    dv = random.randint(1, dice)    #dv=dice value
    print("number = " +str(dv))
    
    return dv

def snakeB(ov, cv, pn):    
    # od=old value, cv=current value, pn=playername
    print("\n" + pn + " snake bite move " + str(ov) + " to " + str(cv))
        
def ladderJ(ov,cv,pn):
     # od=old value, cv=current value, pn=playername
    print("\n" + pn + " ladder jump " + str(ov) + " to " + str(cv))
    
    
def snake_and_ladder(pn,cv,dv):
    ov=cv
    cv=ov+dv
    if cv>maximum_value:
        print(str(cv-maximum_value) + "----------------------need to win")
        return ov
    elif cv in snake:
        fv = snake.get(cv)
        snakeB(cv, fv, pn)
    elif cv in ladder:
        fv = ladder.get(cv)
        ladderJ(cv, fv, pn)   
    else:
        fv = cv
    return fv

def win(pn, position):
    if maximum_value == position:
        print(str( pn.upper()) ,"-----------------------won the game")
        sys.exit(1)
def start():
    player1_cp=0
    player2_cp=0
    player1_name, player2_name = player_names()
    while True:
        input1=input( player1_name +"---------Press enter to roll dice: ")
        dv=dice_value()
        print( player1_name + " moving....")
        player1_cp = snake_and_ladder(player1_name, player1_cp, dv)
        win(player1_name, player1_cp)
        input2=input(player2_name+"-----------Press enter to roll dice: ")
        dv=dice_value()
        print(player2_name + " moving")
        player2_cp = snake_and_ladder(player2_name, player2_cp, dv)
        win(player2_name, player2_cp)

if __name__ == "__main__":
    start()