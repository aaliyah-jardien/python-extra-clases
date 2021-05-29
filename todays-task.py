from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("User Login")


root.mainloop()

username = ["Zoe", "Lihle", "Liyah", "Masi"]
password = ["111", "222", "333", "444"]

name = input("Enter your username:")
key = input("Enter your password:")
found=False

for x in range(len(username)):
    if name == username[x] and key == password[x]:
        found=True

if found==True:
    print("Access Granted")
else:
    print("Access Denied")

