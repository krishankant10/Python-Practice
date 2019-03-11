import tkinter
window=tkinter.Tk()
window.title("Output Window")
window.geometry("300x225")
def onclick():
    print("You pressed +")
bt=tkinter.Button(window, text="+" ,command=onclick())
bt.grid(column=3,row=4)

mysql_connector

