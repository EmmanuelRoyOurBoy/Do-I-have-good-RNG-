import random
PlayerName=str(input("What is your name? "))
OppositionList =["Bob The Builder","Shrek","Waluigi","Emmauel","Another Fire Emblem character","Chris Hansen","R Kelly","Bill Cosby","Anon from 4chan","Naruto","Goku","Reggie Fils-Aimé","Sakurai","Sanic","Brazzers","Etika","Hentai Protagonist"]
Opponent =random.choice(OppositionList)
print("Today you will be facing "+Opponent)
areyouready = False
while areyouready==False:
    QuestionFight=input("Are you READY TO RUMBLE!!!!!!(YES OR NO)")
    if QuestionFight is "YES"or "yes" or "Yes" or "yEs" or  "yeS" or "YeS" or "yES" or "YEs":
        areyouready=True
        break
    elif "NO" or "No" or "nO" or "no":
        areyouready=True
        break
if QuestionFight == "NO" or "No" or "nO" or "no":
    print("Get the fuck outta here.")
