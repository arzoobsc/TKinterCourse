from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")
root.title("Pycharm")


def myfunc():
    print("File Clicked...")

def help():
    print("Help")
    tmsg.showinfo("Help", "Type Your help message here")
def rate():
    print("Rate Us")
    val = tmsg.askquestion("Rate us", "Was your experience Good...")
    print(val)

    if val == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. we will call you soon"
    tmsg.showinfo("Experience", msg)

# # Use this to create non dropdown menu
# my_menu = Menu(root)
# my_menu.add_command(label="File", command=myfunc)
# my_menu.add_command(label="Exit", command=quit)
# root.config(menu=my_menu)

mainmenu =Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)


root.mainloop()
