import tkinter
window =tkinter.Tk()
window.geometry('350x70')

import tkinter
window = tkinter.Tk()
window.title("KK agrawal")
window.geometry('350x70')
label=tkinter.Label(window,text="Hello ! Kk Agrawal").pack()
bt = tkinter.Button(window,text="Enter")
bt.pack()
window.mainloop()

'''
from tkinter import *

master = Tk()

def callback():
    print ("click!")

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()
'''
'''
import tkinter
def clicked():
    print("Button was clicked!!")
window=tkinter.Tk()
bt=tkinter.Button(window,text="Press!",bg="pink",fg="red" ,command=clicked)
bt.pack()
'''
'''
#button value
import tkinter
window=tkinter.Tk()
txt=tkinter.Entry(window,width=10)
txt.grid(column=1,row=0)
def clicked():
    res="Welcome to"+txt.get()
    tkinter.Button.
window.geometry("300x200")
bt=tkinter.Button(window,text="mohan",command=clicked())
bt.grid(column=2,row=2)
'''
'''
#dropdown
import tkinter
from tkinter.ttk import *
window=tkinter.Tk()
window.geometry('300x200')
combo=Combobox(window)
combo['values']=(1,2,3,4,5,"text")
combo.current(1)
combo.grid(column=0,row=0)
'''
'''
#checkbox
import tkinter
window =tkinter.Tk()
chk_state=tkinter.BooleanVar()
chk_state.set(True)
chk=tkinter.Checkbutton(window,text="select",var=chk_state)
chk.grid(column=0,row=0)
'''

'''
#radio button
import tkinter
window=tkinter.Tk()
rad1=tkinter.Radiobutton(window,text='Python',value=1)
rad2=tkinter.Radiobutton(window,text='Java',value=2)
rad3=tkinter.Radiobutton(window,text='Scala',value=3)

rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
'''


'''
#scrolledtext
import tkinter
window =tkinter.Tk()
from tkinter import scrolledtext

txt=scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0,row=0)
'''

'''
#messagebox
from tkinter import messagebox
messagebox.showinfo('Message Title','Message content')
'''

'''
from tkinter import messagebox
def clicked():
    messagebox.showinfo("Message title","Meaage Content")
btn=tkinter.Button(window,text="enter",command=clicked)
btn.grid(column=0,row=0)

'''


#spin box
spin=tkinter.Spinbox(window,from_=0,to=100,width=10)
spin.grid(column=0,row=0)




