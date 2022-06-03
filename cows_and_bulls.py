from tkinter import *
from random import *

root = Tk() #creates a window
root.title("Cows and bulls")
r=randint(1000,9999)
root.counter = 1
root.counter2 = 0


e = Entry(root , width = 35, borderwidth = 5)
e2 = Entry(root,width = 45,borderwidth=5)


e.grid(row = 0 , column = 0 , columnspan = 3, padx = 10, pady = 10)
e2.grid(row = 2 , column = 0 , columnspan = 3 , padx = 10, pady = 10)


def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    e2.delete(0,END)


def clear():
    e.delete(0,END)

def Hint():
    e2.delete(0,END)
    e.delete(0,END)
    m = randint(1,4)
    if root.counter2 == 0 :
        x = "digit",m,"is",str(r)[m-1]
        e2.insert(0,x)
        root.counter2 += 1 
    else:
        e2.insert(0,"you have already used your hint")


def enter():
    cows = 0
    bulls = 0
    n=e.get()
    e.delete(0,END)
    if(int(n)<1000 or int(n)>9999):
        e2.delete(0,END)
        e2.insert(0,"re-enter a 4 digit number")
    
    elif(int(n)!=r):
        for i in range(4):
            x = str(n)
            y = str(r)
            if x[i]==y[i]:
                cows = cows + 1
            elif(x[i] in y):
                bulls = bulls + 1
        root.counter = root.counter + 1
        s = "cows ="+str(cows)+" , bulls ="+str(bulls)
        e2.insert(0,s)
    else:
        v = "congratulations you won , you took "+str(root.counter)+" tries"
        e2.insert(0,v)

#defining the  buttons
bt1 = Button(root, text = "1", padx = 40 , pady = 20,bg="light slate blue",command = lambda :
click(1))
bt2 = Button(root, text = "2", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(2))
bt3 = Button(root, text = "3", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(3))
bt4 = Button(root, text = "4", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(4))
bt5 = Button(root, text = "5", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(5))
bt6 = Button(root, text = "6", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(6))
bt7 = Button(root, text = "7", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(7))
bt8 = Button(root, text = "8", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(8))
bt9 = Button(root, text = "9", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(9))
bt0 = Button(root, text = "0", padx = 40 , pady = 20,bg="light slate blue", command = lambda :
click(0))
btClear = Button(root, text = "Clear", padx = 79 , pady = 20,bg = "deep pink", command =
clear)
btHint = Button(root,text = "Hint",padx = 35,pady = 14,bg="yellow",command = Hint)

btEnter = Button(root, text = "Enter",padx = 140 , pady = 20 ,bg = "forest green", command = enter)

bt1.grid(row = 5, column = 0,padx=5,pady=5)
bt2.grid(row = 5, column = 1,padx=5,pady=5)
bt3.grid(row = 5, column = 2,padx=5,pady=5)
bt4.grid(row = 4, column = 0,padx=5,pady=5)
bt5.grid(row = 4, column = 1,padx=5,pady=5)
bt6.grid(row = 4, column = 2,padx=5,pady=5)
bt7.grid(row = 3, column = 0,padx=5,pady=5)
bt8.grid(row = 3, column = 1,padx=5,pady=5)
bt9.grid(row = 3, column = 2,padx=5,pady=5)
bt0.grid(row = 6, column = 0 )

btClear.grid(row = 6,column = 1,columnspan = 2)
btEnter.grid(row = 7,column=0,columnspan = 3)

btHint.grid(row = 1,column=1)


root.mainloop()
