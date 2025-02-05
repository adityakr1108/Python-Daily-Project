import tkinter
window = tkinter.Tk()
window.title("My Firts GUI")
window.minsize(width=400, height=300)
my_label = tkinter.Label(text = "Hey, I am Aditya", font = ("Arial", 24, "bold"))
# my_label.pack(side = "left") # side = "left" will pack the label to the left side of the window
my_label.pack(expand = 1) # expand = 1 will expand the label to the full window


window.mainloop()