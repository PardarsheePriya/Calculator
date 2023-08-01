from tkinter import *

#function
def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("450x600")
root.title("My Calulator")
root.configure(bg="pink")

#set icon
root.iconbitmap("icon.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="poppins 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

#Number Buttons in frames
#frames: button - line 1
f = Frame(root, bg="#CC3366" )

b = Button(f, text="9", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 4, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="8", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 2, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="7", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 4, pady=6)
b.bind("<Button-1>", click)

f.pack()

#line 2 
#frames: button - line 1
f = Frame(root, bg="#CC3366" )

b = Button(f, text="6", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 4, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="5", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 2, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="4", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 4, pady=6)
b.bind("<Button-1>", click)

f.pack()

#line 3
#frames: button - line 1
f = Frame(root, bg="#CC3366" )

b = Button(f, text="3", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 4, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="2", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 2, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="1", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 4, pady=6)
b.bind("<Button-1>", click)
f.pack()

#0 lines
f = Frame(root, bg="#CC3366" )

b = Button(f, text="+", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 6, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="0", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 2, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="-", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 5, pady=6)
b.bind("<Button-1>", click)

f.pack()

#operation line
f = Frame(root, bg="#CC3366" )

b = Button(f, text="/", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 6, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text="*", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 2, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="%", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 5, pady=6)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="#CC3366" )

b = Button(f, text="=", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 5, pady = 6)
b.bind("<Button-1>", click)

b = Button(f, text=".", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 2, pady=6)
b.bind("<Button-1>", click)

b = Button(f, text="C", bg="pink", padx=18, pady=6, font="poppins 25 bold")
b.pack(side=LEFT, padx= 4, pady=6)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()