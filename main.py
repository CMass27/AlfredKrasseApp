from tkinter import *

root = Tk()
root.title('Alfred Krasse App')
root.iconbitmap("./resources/images/HomeIcon.ico")
root.geometry("400x700")
root['background'] = '#FFFEF6'


def my_click():
    myLabel.destroy()
    myButton.destroy()
    myLabel2.grid(row=0, column=0)


myLabel = Label(root, text="Hello World")
myLabel2 = Label(root, text="For Dennis <3")
myButton = Button(root, text="click me", command=my_click)

myLabel.grid(row=0, column=0)
# myLabel2.grid(row = 1, column = 0)
myButton.grid(row=3, column=0)

root.mainloop()
