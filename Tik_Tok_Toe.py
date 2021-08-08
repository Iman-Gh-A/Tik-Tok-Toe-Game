from tkinter import *


def winPlayer(p):
    text = score.cget("text")
    x = int(text[0])
    o = int(text[-1])
    if p == "X":
        x += 1
        score.configure(text=str(str(x) + "\t" + str(o)))
    else:
        o += 1
        score.configure(text=str(str(x) + "\t" + str(o)))
    if x == 3 or o == 3:
        x, o = 0, 0
        score.configure(text=str(str(x) + "\t" + str(o)))
    deleteButtons()


def deleteButtons():
    for row in range(len(buttons)):
        for column in range(len(buttons[row])):
            buttons[row][column].configure(text="")


def isWinPlayer(r, c):
    if buttons[r][c].cget('text') == buttons[(r + 1) % 3][c].cget('text') == buttons[(r + 2) % 3][c].cget('text') or \
            buttons[r][c].cget('text') == buttons[r][(c + 1) % 3].cget('text') == buttons[r][(c + 2) % 3].cget(
        'text') or \
            buttons[r][c].cget('text') == buttons[(r + 1) % 3][(c + 1) % 3].cget('text') == buttons[(r + 2) % 3][
        (c + 2) % 3].cget('text'):
        winPlayer(buttons[r][c].cget('text'))
    t = True
    for r in buttons:
        for c in r:
            if c.cget("text") == "":
                t = False
    if t:
        deleteButtons()


def pressedButton(r, c):
    global player
    if player == "X":
        buttons[r][c].configure(text=player)
        player = "O"
    else:
        buttons[r][c].configure(text=player)
        player = "X"
    isWinPlayer(r, c)


root = Tk()
root.title("Tik Tok Toe")
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

Label(text="Player 1: X", font=("times new roman", 18)).grid(row=0, column=0)
Label(text="Player 2: O", font=("times new roman", 18)).grid(row=0, column=2)
score = Label(text="0\t0", font=("times new roman", 18))
score.grid(row=0, column=1)

player = "X"

for row in range(len(buttons)):
    for column in range(len(buttons[row])):
        buttons[row][column] = Button(font=("times new roman", 56), bg="blue", width=3,
                                      command=lambda r=row, c=column: pressedButton(r, c))
        buttons[row][column].grid(row=row + 1, column=column)
root.mainloop()
