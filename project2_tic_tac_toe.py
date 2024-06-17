from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

user1=input("name of player 1(x): ")
user2=input("name of player 2 (0): ")

p=tk.Tk()
p.title("TIC_TAC_TOE")
p.configure(background="white")

a=0
ctr=0

board=[]
for i in range(9):
    board.append(0)
print(board)
l2=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def gamecheck(board):

    print(board)
    if 0 not in board:
        print("DRAWW")
        label1.config(text="DRAWW")
    for i in l2:
        flag=0
        for j in i:
            if board[j-1]==0:
                break
            elif board[j-1]==1:
                flag=flag+board[j-1]
            elif board[j-1]==-1:
                flag=flag+board[j-1]
        if flag==3:
            return(1)
        elif flag==-3:
            return(-1)

def destroy():
    button1.config(state="disabled")
    button2.config(state="disabled")
    button3.config(state="disabled")
    button4.config(state="disabled")
    button5.config(state="disabled")
    button6.config(state="disabled")
    button7.config(state="disabled")
    button8.config(state="disabled")
    button9.config(state="disabled")

def work1():
    global ctr

    if ctr%2==0:
        button1.config(text="X",bg="pink")
        button1.config(state="disabled")
        ctr=ctr+1
        board[0]=1
    else:
        
        button1.config(text="O",bg="white")
        button1.config(state="disabled")
        ctr=ctr+1
        board[0]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()

def work2():
    global ctr

    if ctr%2==0:
        button2.config(text="X",bg="pink")
        button2.config(state="disabled")
        ctr=ctr+1
        board[1]=1
    else:
        
        button2.config(text="O",bg="white")
        button2.config(state="disabled")
        ctr=ctr+1
        board[1]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()

def work3():
    global ctr

    if ctr%2==0:
        button3.config(text="X",bg="pink")
        button3.config(state="disabled")
        ctr=ctr+1
        board[2]=1
    else:
        
        button3.config(text="O",bg="white")
        button3.config(state="disabled")
        ctr=ctr+1
        board[2]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()

def work4():
    global ctr

    if ctr%2==0:
        button4.config(text="X",bg="pink")
        button4.config(state="disabled")
        ctr=ctr+1
        board[3]=1
    else:
        
        button4.config(text="O",bg="white")
        button4.config(state="disabled")
        ctr=ctr+1
        board[3]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()

def work5():
    global ctr

    if ctr%2==0:
        button5.config(text="X",bg="pink")
        button5.config(state="disabled")
        ctr=ctr+1
        board[4]=1
    else:
        
        button5.config(text="O",bg="white")
        button5.config(state="disabled")
        ctr=ctr+1
        board[4]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()

def work6():
    global ctr

    if ctr%2==0:
        button6.config(text="X",bg="pink")
        button6.config(state="disabled")
        ctr=ctr+1
        board[5]=1
    else:
        
        button6.config(text="O",bg="white")
        button6.config(state="disabled")
        ctr=ctr+1
        board[5]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()
def work7():
    global ctr

    if ctr%2==0:
        button7.config(text="X",bg="pink")
        button7.config(state="disabled")
        ctr=ctr+1
        board[6]=1
    else:
        
        button7.config(text="O",bg="white")
        button7.config(state="disabled")
        ctr=ctr+1
        board[6]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()

def work8():
    global ctr

    if ctr%2==0:
        button8.config(text="X",bg="pink")
        button8.config(state="disabled")
        ctr=ctr+1
        board[7]=1
    else:
        
        button8.config(text="O",bg="white")
        button8.config(state="disabled")
        ctr=ctr+1
        board[7]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::   "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::   "+user2+"  LOOSER X:: "+user1)
            destroy()

def work9():
    global ctr

    if ctr%2==0:
        button9.config(text="X",bg="pink")
        button9.config(state="disabled")
        ctr=ctr+1
        board[8]=1
    else:
        
        button9.config(text="O",bg="white")
        button9.config(state="disabled")
        ctr=ctr+1
        board[8]=-1
    if ctr>=5:
        ans=gamecheck(board)

        if ans==1:
            print("WINNER X")
            label1.config(text=" WINNER X::    "+user1+"  LOOSER 0:: "+user2)
            destroy()
        elif ans==-1:
            print("WINNER O")
            label1.config(text=" WINNER O::    "+user2+"  LOOSER X:: "+user1)
            destroy()


button1=Button(p,command=work1,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button1.place(x=400,y=100)

button2=Button(p,command=work2,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button2.place(x=600,y=100)

button3=Button(p,command=work3,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button3.place(x=800,y=100)

button4=Button(p,command=work4,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button4.place(x=400,y=250)

button5=Button(p,command=work5,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button5.place(x=600,y=250)

button6=Button(p,command=work6,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button6.place(x=800,y=250)

button7=Button(p,command=work7,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button7.place(x=400,y=400)

button8=Button(p,command=work8,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button8.place(x=600,y=400)

button9=Button(p,command=work9,width=7,height=2,bg="#FFED00",fg="black",borderwidth=3,relief="solid",font=("Helvetica",14))
button9.place(x=800,y=400)

label1=Label(p,width=50,height=2,bg="#ff1a1a",fg="#ffffff",borderwidth=5,relief="solid",font=("Helvetica",20))
label1.place(x=320,y=580)



p.geometry("200x200")
p.state("zoomed")
p.mainloop()
            
            

