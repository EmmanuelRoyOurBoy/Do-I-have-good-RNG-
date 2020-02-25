#This game was made by Emmanuel Roy as a 5 minute coding challenge. The code for this is horrendously bad, so please excuse any errors.
#The game is also fundementally broken when displaying results but that adds onto the RNG element of this game.
import random
Challengers = ["Bob The Builder","Shrek","Waluigi","Another Fire Emblem character","Chris Hansen","Bill Cosby","Anon from 4chan","Reggie Fils-Aimé","Sanic","Brazzers","Hentai Protagonist"]
Opponent =random.choice(Challengers)
P1Name=str(input("What is your name? "))
print(str.format("{} will be facing {}!",P1Name,Opponent))
RandomNumber = int(random.randint(1,101))
P1ChosenNumber = int(input("Pick a number from 1-100! "))
OpponentChosenNumber = int(random.randint(1,101))
print(str.format("{} chose {} and {} chose {}! ", P1Name, P1ChosenNumber, Opponent, OpponentChosenNumber))
print(str.format("The number was {}", RandomNumber))
if (P1ChosenNumber - RandomNumber) >= (OpponentChosenNumber - RandomNumber) or (RandomNumber - P1ChosenNumber) <= (RandomNumber - OpponentChosenNumber):
    print(str.format("{} wins!",P1Name))
else:
    print(str.format("{} wins!",Opponent))
