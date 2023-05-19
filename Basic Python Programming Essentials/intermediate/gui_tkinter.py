from tkinter import * #used to import tkinter.

mainWindow = Tk() #Tk() constructor for a window .

topFrame = Frame(mainWindow) #Frame() creates a frame for the interface. An invisible rectangle.
topFrame.pack() #pack() places widget into the interface.

botFrame = Frame(mainWindow)
botFrame.pack(side=BOTTOM) #side for positioning.

btn1 = Button(topFrame, text="Button 1", fg="red")
btn2 = Button(topFrame, text="Button 2", fg="green")
btn3 = Button(botFrame, text="Button 3", fg="blue")
btn4 = Button(botFrame, text="Button 4", fg="yellow")
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()


mainWindow.mainloop() #mainloop keeps the window open until the user closes it.