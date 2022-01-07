import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.messagebox import showinfo
from dataclasses import dataclass, InitVar

@dataclass
class ScreenData:
    zone_id: str
    zone_name: str
    zone_status: bool

    # def get_zone_info(self):
    #     zone_info = [self.zone_id.get(),self.zone_name.get(), self.zone_status.get()]
    #     return zone_info

    # def set_zone_info(self, zone_info: list) -> None:
    #     self.zone_id.set(zone_info[0])
    #     self.zone_name.set(zone_info[1])
    #     self.zone_status.set(zone_info[2])

    def set_zone_name(self, zone_name):
        self.zone_name = zone_name

    def get_zone_name(self):
        return self.zone_name

    def set_zone_id(self, zone_id):
        self.zone_id = zone_id

    def get_zone_id(self):
        return self.zone_id

    def set_zone_status(self, zone_status):
        self.zone_status = zone_status

    def get_zone_status(self):
        return self.zone_status


class TreeViewContainer(tk.Frame, ScreenData):
    def __init__(self):
        super().__init__()

        self.zone_id_sv = StringVar(value=self.zone_id)
        self.zone_name_sv = StringVar(value=self.zone_name)
        self.zone_status_sv = StringVar(value=self.zone_status)

    def draw_widget(self):
        columns = ['name', 'id', 'status']

        self.my_tree = ttk.Treeview(self, columns=columns, show='headings')
        self.my_tree.heading('name', text='Name')
        self.my_tree.heading('id', text='Id')
        self.my_tree.heading('status', text='Status')

        zones = []
        
        zones.append((self.zone_name_sv.get(), self.zone_id_sv.get(), self.zone_status_sv.get()))

        for zone in zones:
            self.my_tree.insert('', tk.END, values=zone)

        self.my_tree.bind('<<TreeviewSelect>>', self._item_selected)
        self.my_tree.grid(row=1, column=0, columnspan=2)
        self.grid(row=1 , column=0)
    
    def _item_selected(self, event):
        
        for selected_item in self.my_tree.selection():
            item = self.my_tree.item(selected_item)
            record = item['values']
            # showinfo(title='Info', message=','.join(record))
            self.zone_name_sv.set(record[0])
            self.zone_id_sv.set(record[1])
            self.zone_status_sv.set(record[2])

class OptionsContainer(tk.Frame, ScreenData):
    def __init__(self, ):
        super().__init__()
        
        self.zone_id_sv = StringVar(value=self.zone_id)
        self.zone_name_sv = StringVar(value=self.zone_name)
        self.zone_status_sv = StringVar(value=self.zone_status)


    def draw_widget(self):
        lbl_zone_name = tk.Label(self, text='Zone Name')
        txt_zone_name = tk.Entry(self, textvariable=self.zone_name_sv)
        lbl_zone_name.grid(row=0, column=0)
        txt_zone_name.grid(row=0, column=1)

        lbl_zone_id = tk.Label(self, text='Zone Id')
        txt_zone_id = tk.Entry(self, textvariable=self.zone_id_sv)
        lbl_zone_id.grid(row=1, column=0)
        txt_zone_id.grid(row=1, column=1)

        lbl_zone_status = tk.Label(self, text='Zone status')
        txt_zone_status = tk.Entry(self, textvariable=self.zone_status_sv)
        lbl_zone_status.grid(row=2, column=0)
        txt_zone_status.grid(row=2, column=1)
        self.grid(row=0, column=0)

    


