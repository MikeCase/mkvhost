import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class TreeViewContainer(tk.Frame):
    def __init__(self, zone_name, zone_id, zone_status):
        super().__init__()

        self.zone_name = zone_name
        self.zone_id = zone_id
        self.zone_status = zone_status


    def draw_widget(self, my_zones):
        columns = ['name', 'id', 'status']

        self.my_tree = ttk.Treeview(self, columns=columns, show='headings')
        self.my_tree.heading('name', text='Name')
        self.my_tree.heading('id', text='Id')
        self.my_tree.heading('status', text='Status')

        zones = []
        for zone in my_zones['result']:
            zones.append((zone['name'], zone['id'], zone['status']))

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
            self.zone_name.set(record[0])
            self.zone_id.set(record[1])
            self.zone_status.set(record[2])

class OptionsContainer(tk.Frame):
    def __init__(self, ):
        super().__init__()
        self.zone_name_sv = tk.StringVar()
        self.zone_id_sv = tk.StringVar()
        self.zone_status_sv = tk.StringVar()


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

    def set_zone_name(self, zone_name):
        self.zone_name_sv.set(zone_name)

    def get_zone_name(self):
        return self.zone_name_sv.get()

    def set_zone_id(self, zone_id):
        self.zone_id_sv.set(zone_id)

    def get_zone_id(self):
        return self.zone_id_sv.get()

    def set_zone_status(self, zone_status):
        self.zone_status_sv.set(zone_status)

    def get_zone_status(self):
        return self.zone_status_sv.get()
