import tkinter as tk
from tkinter import ttk
from controllers.controllers import Controller, ZoneController
from gui.views import Form, TreeViewForm


class Application(ttk.Notebook):
    """ Setup Application Instance """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky='nsew')

    def new_tab(self, controller: Controller, view: Form, name: str):
        view = view(self.master)
        controller.bind(view)
        self.add(view, text=name)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)

    zone_controller = ZoneController()
    app.new_tab(controller=zone_controller, view=Form, name='First Tab')
    app.new_tab(controller=zone_controller, view=)

    app.mainloop()