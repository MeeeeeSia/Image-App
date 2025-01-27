from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import Image
image_idk = 'Test.png'

image = Image.open(image_idk)



def hello_world():
   print('hello world')

def b_w():
   bw = image.convert('L')


win = Tk()
win.geometry("700x350")


def open_prompt():
   messagebox.showinfo("Message", "Click Okay to Proceed")


Label(win, text= "Click to Open the MessageBox").pack(pady=15)



ttk.Button(win, text= "Open", command= hello_world).pack()

win.mainloop()

