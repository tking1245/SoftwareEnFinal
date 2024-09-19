import tkinter as tk
from PIL import Image, ImageTk
import RealStats as rs

def show_sidebar(event):
    """Show the sidebar and hide the menu icon when hovering over the menu icon."""
    menu_icon.place_forget()  # Hide the menu icon
    sidebar.place(x=5, y=5)   # Show the sidebar with an offset to simulate a shadow

def hide_sidebar(event):
    """Hide the sidebar and show the menu icon when moving away from the sidebar."""
    sidebar.place_forget()    # Hide the sidebar
    menu_icon.place(x=10, y=10)  # Show the menu icon again

########### HISTORY DATA WINDOW

def run_historic_data_window():

    hisWin = tk.Tk()
    hisWin.mainloop()
    return 








# Create the main window
window = tk.Tk()
window.title('Landing Page')
window.geometry('900x600')

# Load and resize the image
examplegraph = Image.open('dummyGr.png')
resize_graph = examplegraph.resize((150, 100))
newimggr = ImageTk.PhotoImage(resize_graph)

# Buttons for stocks
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
sidebar = tk.Frame(window, width=200, height=600 , bd=2, relief = 'solid')  # Raised border

# Sidebar buttons or options
sidebar_button1 = tk.Button(sidebar, text="Trading Practice", relief="sunken", fg="Black", font=("Times", 12))
sidebar_button1.pack(pady=10, padx=10, fill='x')
sidebar_button2 = tk.Button(sidebar, text="Option 2", relief="flat",command = run_historic_data_window, fg="Black", font=("Arial", 12))
sidebar_button2.pack(pady=10, padx=10, fill='x')
sidebar_button3 = tk.Button(sidebar, text="Option 3", relief="flat", fg="Black", font=("Arial", 12))
sidebar_button3.pack(pady=10, padx=10, fill='x')

# Create the icon on the left for hovering (menu icon)
menu_icon = tk.Button(window, text="☰", font=("Arial", 16), bg="grey", fg="white", relief="flat")
menu_icon.place(x=10, y=10)

# Bind hover event to show the sidebar and hide the menu icon
menu_icon.bind("<Enter>", show_sidebar)

# Bind event to hide the sidebar and show the menu icon again when mouse leaves the sidebar
sidebar.bind("<Leave>", hide_sidebar)

# Set the window's background color
window.config(background='DarkSlateGrey')


window.mainloop()

