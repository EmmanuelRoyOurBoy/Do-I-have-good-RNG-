import random
PlayerName=str(input("What is your name? "))
OppositionList =["Bob The Builder","Shrek","Waluigi","Emmauel","Another Fire Emblem character","Chris Hansen","R Kelly","Bill Cosby","Anon from 4chan","Naruto","Goku","Reggie Fils-Aimé","Sakurai","Sanic","Brazzers","Etika","Hentai Protagonist"]
Opponent =random.choice(OppositionList)
print("Today you will be facing "+Opponent)
QuestionFight=input("Are you READY TO RUMBLE!!!!!!(YES OR YES)")
areyouready = False
if QuestionFight == "YES"or "yes" or "Yes" or "yEs" or  "yeS" or "YeS" or "yES" or "YEs":
    areyouready=True
if areyouready == True:
    print("Lets begin then")
