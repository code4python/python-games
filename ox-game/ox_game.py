from tkinter import *
import random

def next_turn(row ,col):
    global player
    if  gam_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            """put player 1"""
            gam_btns[row][col]['text'] = player

            if check_winner() == False:
                player = players[1]
                lable.config(text=(players[1] + " Turn"))

            elif check_winner() == True:
                lable.config(text=(players[0]+ " Win!"))

            elif check_winner() == "tie":
                lable.config(text="Tie,No Winner!")

 #   """two player opction"""

        elif player == players[1]:
            """ptu plyer 2"""
            gam_btns[row][col]['text'] = player

            if check_winner() == False:
                player = players[0]
                lable.config(text=(players[0] + " Turn"))

            elif check_winner() == True:
                lable.config(text=(players[1]+ " Winner!"))


            elif check_winner() == "tie":
                lable.config(text="Tie , No Winner!")


def check_winner():
    # chack winner 
    for row in range(3):
        if gam_btns[row][0]['text'] == gam_btns[row][1]['text'] == gam_btns[row][2]['text'] != "":
            gam_btns[row][0].config(bg="green")
            gam_btns[row][1].config(bg="green")
            gam_btns[row][2].config(bg="green")
            return True
        
    for col in range(3):
        if gam_btns[0][col]['text'] == gam_btns[1][col]['text'] == gam_btns[2][col]['text'] != "":
            gam_btns[0][col].config(bg="green")
            gam_btns[1][col].config(bg="green")
            gam_btns[2][col].config(bg="green")
            return True
        
    # ckach dyagnals ;
    if gam_btns[0][0]['text'] == gam_btns[1][1]['text'] == gam_btns[2][2]['text'] != "":
        gam_btns[0][0].config(bg="green")
        gam_btns[1][1].config(bg="green")
        gam_btns[2][2].config(bg="green")
        return True
    elif gam_btns[0][2]['text'] == gam_btns[1][1]['text'] == gam_btns[2][0]['text'] != "":
        gam_btns[0][2].config(bg="green")
        gam_btns[1][1].config(bg="green")
        gam_btns[2][0].config(bg="green")
        return True
    
    """cheak three are no empy spasses left"""
    if check_empty_spases() == False:
        for row in range(3):
            for col in range(3):
                gam_btns[row][col].config(bg="red")

        return "tie"
    else:
        return False
    
def check_empty_spases():
    spase= 9
    for row in range(3):
        for col in range(3):
            if gam_btns[row][col]['text'] != "":
                spase -= 1
    if spase == 0:
        return False
    else:
        return True

def start_new_game():
    global player
    player = random.choice(player)
    lable.config(text=(player + " Turn"))
    for row in range(3):
        for col in range(3):
            gam_btns[row][col].config(text="", bg="#F0F0F0")


window = Tk()

window.title("Tic Tac Toe | Ahmed pro")
window.positionfrom("program")
players = ["x", "o"]
player = random.choice(players)

gam_btns = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
lable = Label(text=(player + " Turn"), font=("consolas",40))
lable.pack(side="top")

restart_btn = Button(text="restart", font=("consolas",40), command=start_new_game )
restart_btn.pack(side="top")

btn_frame = Frame()
btn_frame.pack()

for row in range(3):
    for col in range(3):
        gam_btns[row][col] = Button(btn_frame,text="" ,font=("consolas",50),width=4, height=1,command= lambda row=row, col=col: next_turn(row, col))
        gam_btns[row][col].grid(row=row,column=col)



window.mainloop()