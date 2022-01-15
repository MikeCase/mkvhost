import tkinter as tk
from tkinter import ttk
from gui.views import View


class SubdomainView(View):
    def __init__(self, master=None, model=None):
        super().__init__(master)

        self.master = master
        self.model = model

        self.padx = 5
        self.pady = 10
        self.sticky = tk.N + tk.S + tk.E + tk.W
        
        self.entries = {}
        self.buttons = {}

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, padx=self.padx)

    def create_view(self):
        
        edit_info_frame = ttk.LabelFrame(master=self, text='Edit Subdomain')
        edit_info_frame.grid(row=0, column=0, padx=self.padx, pady=self.pady)
        list_subdomains_frame = ttk.LabelFrame(master=self, text='Available Subdomains')
        list_subdomains_frame.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        ## Everything that should go inside the edit info frame
        self.create_lbl_entry(edit_info_frame, 'Record ID: ', 0, 1, self.model.record_id)
        self.create_lbl_entry(edit_info_frame, 'Record Type: ', 1, 1, self.model.record_type)
        self.create_lbl_entry(edit_info_frame, 'Record Name: ', 2, 1, self.model.record_name)
        self.create_lbl_entry(edit_info_frame, 'Record Name: ', 0, 3, self.model.record_name)
        self.create_lbl_entry(edit_info_frame, 'Record Name: ', 1, 3, self.model.record_name)


        ## Everything that should go in the list subdomains frame
        self.create_listbox(list_subdomains_frame, ['one', 'two', 'three', 'four'], 0, 0)

    def create_listbox(self, frame, listvar, row, col):
        lb_height = len(listvar)
        listbox = tk.Listbox(master=frame, listvariable=listvar,  height=lb_height)
        listbox.grid(row=row, column=col)