import tkinter as tk
from tkinter import ttk
from controllers.controllers import Controller
from controllers.form_controller import FormController
from controllers.subdomain_controller import SubdomainController
from controllers.zone_controller import ZoneController
from controllers.settings_controller import SettingsController
from gui.form_view import Form
from gui.subdomain_view import SubdomainView
from gui.tree_view import TreeViewForm
from gui.settings_view import SettingsView
from models.models import CloudFlare


class Application(ttk.Notebook):
    """ Setup Application Instance """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.model = CloudFlare()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky='nsew')

    def new_tab(self, controller: Controller, view: Form, name: str):
        view = view(self.master)
        controller.bind(view, self.model)
        self.add(view, text=name)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Vhost Creator')
    app = Application(master=root)
    # cflare = CFlare()

    form_controller = FormController()
    zone_controller = ZoneController()
    subd_controller = SubdomainController()
    settings_controller = SettingsController()

    app.new_tab(controller=zone_controller, view=TreeViewForm, name='Available Zones')
    app.new_tab(controller=subd_controller, view=SubdomainView, name='Available Subdomains')
    app.new_tab(controller=form_controller, view=Form, name='Input Tab')
    app.new_tab(controller=settings_controller, view=SettingsView, name='Settings')

    app.mainloop()