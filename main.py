from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image
image_idk = 'C:\\Users\\Lenovo\\Desktop\\Python\\Image-App\\test.png'

image = Image.open(image_idk)


def open_prompt():
   messagebox.showinfo("Message", "Click Okay to Proceed")


def update_label(value):
    label.config(text=f"Value: {value}")

def hello_world():
   print('hello world')

def b_w():
   bw = image.convert('L')


win = Tk()
win.geometry("700x350")
image = PhotoImage(file='C:\\Users\\Lenovo\\Desktop\\Python\\Image-App\\test.png')

scale_var = IntVar()
scale_var.set(50)
# Create a ttk Scale widget with variable and command options
scale = ttk.Scale(win, from_=0, to=100, length=300, variable=scale_var, command=update_label)
scale.pack()
label =ttk.Label(win, text="Value: 50")
label.pack()
image_label = ttk.Label(win, image=image)
image_label.pack()

Label(win, text= "Click to Open the MessageBox").pack(pady=15)



ttk.Button(win, text= "Open", command= hello_world).pack()

win.mainloop()

