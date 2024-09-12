import tkinter as tk
from PIL import Image, ImageTk

def show_sidebar(event):
    """Function to show the side bar when mouse hovers over the icon."""
    menu_icon.place_forget()  # Hide the menu icon
    sidebar.place(x=0, y=0)

def hide_sidebar(event):
    """Function to hide the side bar when mouse moves away."""
    sidebar.place_forget()    # Hide the sidebar
    menu_icon.place(x=10, y=10)

# window settings 
window = tk.Tk()
window.title('Landing Page')
window.geometry('900x600')

# image size
examplegraph = Image.open('dummyGr.png')
resize_graph = examplegraph.resize((150, 100))
newimggr = ImageTk.PhotoImage(resize_graph)

# Buttons
stockbutton = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton.place(x=80, y=50)
stockbutton1 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton1.place(x=370, y=50)
stockbutton2 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton2.place(x=660, y=50)
stockbutton3 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton3.place(x=80, y=290)
stockbutton4 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton4.place(x=370, y=290)
stockbutton5 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton5.place(x=660, y=290)

# Create a frame for the sidebar on the left
sidebar = tk.Frame(window, width=175, height=250, bg="grey")
# Sidebar buttons or options
sidebar_button1 = tk.Button(sidebar, text="Trading Practice")
sidebar_button1.place(x = 10, y = 10)
sidebar_button2 = tk.Button(sidebar, text="Option 2")
sidebar_button2.place(x = 10, y = 40)
sidebar_button3 = tk.Button(sidebar, text="Option 3")
sidebar_button3.place(x = 10, y = 70)

sidebar_button1.configure(background = 'DarkSlategrey')


menu_icon = tk.Button(window, text="☰", font=("Arial", 16), bg="DarkSlategrey", fg="grey44")
menu_icon.place(x=10, y=10)

# Bind hover event to show the sidebar when the mouse enters the icon
menu_icon.bind("<Enter>", show_sidebar, )
# Bind event to hide the sidebar when the mouse leaves
sidebar.bind("<Leave>", hide_sidebar)

# Set the window's background color
window.config(background='DarkSlategrey')



# Run the main loop
window.mainloop()
