from tkinter import *

root = Tk()
root.geometry("733x566")
root.title("Pycharm")


def myfunc():
    print("File Clicked...")

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


root.mainloop()
