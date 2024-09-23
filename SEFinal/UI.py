import tkinter as tk
from PIL import Image, ImageTk
import RealStats as rstat

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
    """Open a new window for historic data input."""
    hisWin = tk.Tk()
    hisWin.geometry('300x200')
 
    # Input fields for stock and time frame
    timeFrame = tk.Entry(hisWin, width=20)
    stockinput = tk.Entry(hisWin, width=20)

    # Define command for button
    def grab_data():
        # Call rstat.create_graph with the user input
        stock = stockinput.get()
        time = timeFrame.get()
        rstat.create_graph(stock, time)

    # Button to trigger the graph creation
    getinfo = tk.Button(hisWin, text="Grab", compound="bottom", background='white', command=grab_data)
    
    # Layout widgets
    stockinput.pack(pady=8)
    timeFrame.pack(pady=15)
    getinfo.pack(pady=25)
    
    hisWin.mainloop()

# Create the main window
window = tk.Tk()
window.title('Landing Page')
window.geometry('900x600')

# Load and resize the image
examplegraph = Image.open('dummyGr.png')
resize_graph = examplegraph.resize((150, 100))
newimggr = ImageTk.PhotoImage(resize_graph)

# Buttons for stocks with images
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
sidebar = tk.Frame(window, width=200, height=600, bd=2, relief='solid')  # Raised border

# Sidebar buttons or options
sidebar_button1 = tk.Button(sidebar, text="Trading Practice", relief="sunken", fg="Black", font=("Times", 12))
sidebar_button1.pack(pady=10, padx=10, fill='x')
sidebar_button2 = tk.Button(sidebar, text="Option 2", relief="flat", command=run_historic_data_window, fg="Black", font=("Arial", 12))
sidebar_button2.pack(pady=10, padx=10, fill='x')
sidebar_button3 = tk.Button(sidebar, text="Option 3", relief="flat", fg="Black", font=("Arial", 12))
sidebar_button3.pack(pady=10, padx=10, fill='x')

# Menu icon button
menu_icon = tk.Button(window, text="☰", font=("Arial", 16), bg="grey", fg="white", relief="flat")
menu_icon.place(x=10, y=10)

# Bind events for sidebar and menu icon
menu_icon.bind("<Enter>", show_sidebar)
sidebar.bind("<Leave>", hide_sidebar)

# Set window background
window.config(background='DarkSlateGrey')

# Run the application
window.mainloop()
