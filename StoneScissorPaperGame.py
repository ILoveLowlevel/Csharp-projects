import random
from easygui import *
Generate_GameObject1 = random.randint(1,3)
Generate_GameObject2 = random.randint(1,3)
GameObjects = ["NULL","Tas","Kagit","Makas"]
WinnerPlayer = 0
## 1 - Player1 | 2 - Player2 | 0 - no win
"""
------------------
Tas > Makas
Kagit > Tas
Makas > Kagit
------------------
1 > 3
2 > 1
3 > 2
------------------
"""
text = "text"
title = "title"
d_text = ""
output = enterbox(text,title,d_text)
title = "Message Box"
message = "Entered Name : " + str(output)
msg = msgbox(message,title)



print("PLAYER1"+GameObjects[Generate_GameObject1])
print("PLAYER2"+GameObjects[Generate_GameObject2])
def GameWhoisWon(player1,player2):
    ListDataWinSituationsp1 = ["NULL","1-3","2-1","3-2"]
    ListDataWinSituationsp2 = ["NULL","3-1","1-2","2-3"]
    ListDataNoWinSituationsp1p2 = ["1-1","2-2","3-3"]
    ## 1,2,3 => P1 4,5,6 => P2
    winner = 0
    Data_of_WinSituations = str(player1) + "-" + str(player2)
    for data in ListDataWinSituationsp1:
        if (Data_of_WinSituations == data):
            winner = 1
            break
    for data2 in ListDataWinSituationsp2:
        if (Data_of_WinSituations == data2):
            winner = 2
            break
    for data3 in ListDataNoWinSituationsp1p2:
        if (Data_of_WinSituations == data3):
            winner = 0
            break
    return winner

WinnerPlayer = GameWhoisWon(Generate_GameObject1,Generate_GameObject2)
if (WinnerPlayer == 1):
    msgbox("PLAYER1 is WINNER")
if (WinnerPlayer == 2):
    msgbox("PLAYER2 is WINNER")

