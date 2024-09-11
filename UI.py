import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Landing Page')
window.geometry('900x600')
examplegraph = Image.open('dummyGr.png')
resize_graph = examplegraph.resize((150,100))
newimggr = ImageTk.PhotoImage(resize_graph)

stockbutton = tk.Button(window, text = "Name of Stock" , image = newimggr, compound = 'top')


#


# Compiling the Window and its contents
stockbutton.size()
stockbutton.pack(side = 'left', padx = 25 ,pady=0)
window.mainloop()