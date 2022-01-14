import tkinter as tk
from tkinter import ttk
from abc import abstractmethod
from typing import List
from tkinter.messagebox import showinfo

class View(tk.Frame):

    @abstractmethod
    def create_view():
        raise NotImplementedError

    def create_lbl_entry(self, frame, label, row, column, textvar):
        """Create entry with label next to it."""

        label = tk.Label(frame, text=label)
        self.entries[label] = tk.Entry(frame, textvariable=textvar)
        self.entries[label].grid(row=row, column=column, sticky=self.sticky, padx=self.padx, pady=self.pady)
        label.grid(row=row, column=column-1, sticky=self.sticky, padx=self.padx, pady=self.pady)



    # def create_lbl_frm(self, frame, label, row, column):
    #     """ Create new label frame """

    #     lblframe = ttk.LabelFrame(frame, text=label)
    #     lblframe.grid(row=row, column=column, padx=self.padx, pady=self.pady)



    def create_btn(self, frame, name, row, column):
        """ Create button """

        self.buttons[name] = tk.Button(frame)
        self.buttons[name]['text'] = name
        self.buttons[name].grid(row=row, column=column,)



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
                showinfo(message=self.model.get_dns_records(self.model.zone_id.get()))