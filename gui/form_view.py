from gui.views import View
import tkinter as tk
from tkinter import ttk

class Form(View):
    def __init__(self, master=None, model=None):
        super().__init__(master)
        self.master = master
        self.model = model

        self.padx = 10
        self.pady = 5
        self.sticky = tk.N + tk.S + tk.E + tk.W

        self.entries = {}
        self.buttons = {}
        self.labels = {}

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=self.sticky)

    def create_view(self):
        
        input_frame = ttk.LabelFrame(master=self, text='Input Data')
        input_frame.rowconfigure(4, weight=1)
        input_frame.columnconfigure(3, weight=1)
        input_frame.grid(row=0, column=0, sticky=self.sticky, padx=self.padx, pady=self.pady)

        self.create_lbl_entry(input_frame, 'Zone Id', 0, 1, self.model.zone_id)
        self.create_lbl_entry(input_frame, 'Zone Name', 1, 1, self.model.zone_name)
        self.create_lbl_entry(input_frame, 'Zone Status', 2, 1, self.model.zone_status)
        
        self.create_btn(input_frame, 'Add', 3, 0)
        self.create_btn(input_frame, 'Update', 3, 1)
        self.create_btn(input_frame, 'Delete', 3, 2)