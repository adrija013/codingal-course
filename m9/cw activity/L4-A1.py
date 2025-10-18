from tkinter import *

window = Tk()
window.title('Tkinter sample window')
window.geometry('300x300')

greeting = Label(text="Hello user",fg='black',bg='white')
button = Button(text="Click me",bg='black',fg='white')
entry = Entry(fg="yellow",bg="blue",width=100)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='green', bg='white')
textbox.pack()

window.mainloop()