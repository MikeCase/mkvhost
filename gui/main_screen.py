import tkinter as tk
from settings_screen import SettingsScreen
# import os
# import dotenv

class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('mkVhost')
        self.geometry('800x600')

        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: self.doNothing())
        filemenu.add_separator()
        filemenu.add_command(label="Settings", command=lambda: self.settings())
        menubar.add_cascade(label="File", menu=filemenu)

        container = tk.Frame(self)
        container.grid(row=0, column=0)

        self.config(menu=menubar)

    def doNothing(self):
        print("Did Nothing")

    def settings(self):
        # dotenv.load_dotenv()
        return SettingsScreen() 
        
if __name__ == '__main__':
    app = MainScreen()
    app.mainloop()
        