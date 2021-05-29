from tkinter import *

root = Tk()
root.title("Weekend Classes")
root.geometry("500x500")
root.config(bg="purple")

lab_1 = Label(root, text="Please enter first number", bg="pink")
lab_1.place(x=40, y=20)
txt_entry1 = Entry(root)
txt_entry1.place(x=250, y=20)

lab_2 = Label(root, text="Please enter second number", bg="pink")
lab_2.place(x=40, y=60)
txt_entry2 = Entry(root)
txt_entry2.place(x=250,y=60)

myresult=StringVar()
lab_3 = Label(root, text="", textvariable=myresult, width="20", bg="white")
lab_3.place(x=150, y=120)

def addition():
    answer=int(txt_entry1.get())+int(txt_entry2.get())
    myresult.set(answer)

btn_add = Button(root, text="Add", bg="pink", command=addition)
btn_add.place(x=50, y=180)

def clear():
    txt_entry1.delete(0, END)
    txt_entry2.delete(0, END)
    myresult.set("")

btn_clear = Button(root, text="Clear", bg="pink", command=clear)
btn_clear.place(x=150, y=180)

def exit():
    return root.destroy()

btn_exit = Button(root, text="Exit", bg="pink", command=exit)
btn_exit.place(x=200, y=180)

root.mainloop()
