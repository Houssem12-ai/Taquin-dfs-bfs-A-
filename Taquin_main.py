# Author: idrisso4
# Main file


# Importing libraries
from tkinter import *
import time
from Solver import Solver
from Solver import Node
from Solver import Puzzle

global puzzl
global Lph , LAff


# Defining interface parameters
fenetre = Tk()

board = [[1,2,3],[4,8,5],[7,0,6]]

photos=[]
for i in range(0,10):
	photos.append(PhotoImage(file="./images/"+str(i)+".png"))
Lph = photos[0:9]

can=Canvas( width=180*3,height=180*3,bg='white')
can.pack( side =TOP, padx =20, pady =20)
fenetre['bg']='white'
fenetre.title (' Taquin resolution IA')

puzzl = Puzzle(board,can,Lph)


# Defining functions
def solv_larg():
	s =Solver(puzzl,fenetre)
	s.solve_Larg()

def solv_long():
	s =Solver(puzzl,fenetre)
	s.solve_Long()

def solve_a_étoile():
        s =Solver(puzzl,fenetre)
        s.solve_a_etoile()

def mel():
	global puzzl
	puzzl = puzzl.shuffle()


LAff=[]
for row in board:
    LAff.extend(row)

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Search in width (BFS)", command=solv_larg)
menu1.add_command(label="Search in length (DFS)", command=solv_long)
menu1.add_command(label="A*", command=solve_a_étoile)
menubar.add_cascade(label="Solve", menu=menu1)
fenetre.config(menu=menubar)



Button(text='Mix',command=mel).pack(side=LEFT)
Button(text='Exit',command=fenetre.quit).pack(side=RIGHT)


for k in range(len(Lph)) :
    eff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW, image=Lph[0])
    aff = can.create_image((30+ 150*(k % 3)), 30+(150*( k // 3)), anchor=NW ,image = Lph[LAff[k]])

can.pack()

fenetre.mainloop()
