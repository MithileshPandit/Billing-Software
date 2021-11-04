import tkinter as tk

def showFrame(frame):
    frame.tkraise()

window = tk.Tk()
window.state('zoomed')

megaFrame = tk.Frame(window)
megaFrame.place(x=15,y=15,width=25,height=25)
frame1 = tk.Frame(megaFrame)
button = tk.Button(frame1,text="Heelo").pack()

frame2 = tk.Frame(megaFrame)

for frame in (frame1,frame2):
    frame.grid(row=0,column=0,sticky='nsew')

showFrame(frame1)
# showFrame(frame2)
window.mainloop()