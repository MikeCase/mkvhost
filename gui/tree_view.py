from gui.views import View
import tkinter as tk
from tkinter import ttk
from  typing import List

class TreeViewForm(View):
    def __init__(self, master=None, model=None):
        super().__init__(master)
        self.master = master

        self.padx = 10
        self.pady = 5
        self.sticky = tk.N + tk.S + tk.E + tk.W

        self.model = model

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=self.sticky)

    def create_view(self, zones: list, zone_data: list):
        self.controller = None
        tree_frame = ttk.LabelFrame(master=self, text='Available Zones')
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        tree_frame.grid(row=0, column=0, sticky=self.sticky, padx=self.padx, pady=self.pady)

        self.create_treeview(tree_frame, zones, zone_data, 0, 0)

    def create_treeview(self, frame: tk.LabelFrame, headings: list, zones: List[tuple], row: int, column: int):
        """Create TreeView
        
            frame = What frame is this going in? 
            row = What row in a grid geometry?
            columm = What Column in a grid geometry?
            headings = The headings to be displayed (all lowercase names)

        """
        tree = ttk.Treeview(frame, columns=headings, show='headings')
        tree.columnconfigure(0, weight=1)
        tree.rowconfigure(0, weight=1)
        for col_name in headings:
            tree.heading(col_name, text=col_name.capitalize())
        tree.bind('<<TreeviewSelect>>', lambda x: _item_selected())
        tree.grid(row=row, column=column)

        for zone in zones:
            tree.insert('', tk.END, values=zone)

        def _item_selected():
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                self.model.zone_id.set(record[0])
                self.model.zone_name.set(record[1])
                self.model.zone_status.set(record[2])