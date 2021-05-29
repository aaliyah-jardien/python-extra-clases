from tkinter import *

root = Tk()
root.title("Weekend Classes")
root.geometry("500x500")
root.config(bg="black")

myframe = Frame(root)
myframe.place(x=0, y=0, width=500, height=500)

Label_text = StringVar()

lab_1 = Label(root, text="Enter your username: ", bg="aqua")
lab_1.place(x=40, y=20)
txt_entry1 = Entry(root)
txt_entry1.place(x=250, y=20)

lab_2 = Label(root, text="Enter your password: ", bg="aqua")
lab_2.place(x=40, y=60)
txt_entry2 = Entry(root)
txt_entry2.place(x=250,y=60)

# myresult=StringVar()
# lab_3 = Label(root, text="", textvariable=myresult, width="20", bg="white")
# lab_3.place(x=150, y=120)
def membership():
    username = ["Zoe", "Lihle", "Liyah", "Masi"]
    password = ["111", "222", "333", "444"]
    found = False

    for x in range(len(username)):
        if txt_entry1 == username[x] and txt_entry2 == password[x]:
            found = True
    if found == True
        messagebox.shadowinfo("ACCESS INFO", "Access Granted")
        root.destroy()
        import randoms_num
    else:
        messagebox.shadowerror("ACCESS ERROR", "Access Denied")

def exit_button():
    return root.destroy()

mybutton = Button(myframe, tetx="Enter", command=membership)
mybutton.place(x=155, y=155)
but1 = Button(myframe, text="Enter", command=exit_button)
but1.place(x=255, y=155)

root.mainloop()
