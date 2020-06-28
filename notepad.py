from tkinter import *

if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("644x788")

    # Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None

    # Lets create a menubar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)

    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    # To open already exiting file
    FileMenu.add_command(label="Open", command=openFile)


    root.mainloop()