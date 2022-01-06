import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from cloudflare.cflare import CFlare
from gui.settings_screen import SettingsScreen
# from cloudflare.cflare import CFlare

class MainScreen(tk.Tk):
    def __init__(self, cflare: CFlare):
        super().__init__()
        
        
        
        self.cflare = cflare
        self.zones = self.cflare.show_zones()
        self.title('mkVhost')
        self.geometry('800x600')

        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: self.doNothing())
        filemenu.add_separator()
        filemenu.add_command(label="Settings", command=lambda: self.settings(self.zones))
        menubar.add_cascade(label="File", menu=filemenu)
        # print(cflare.show_zones())

        container = tk.Frame(self)
        container.grid(row=0, column=0)

        self.build_widget_frame()
        if self.zones == None:
            self.settings(self.zones)
        else:
            self.build_treeview(container, 0, 0)

        self.config(menu=menubar)

    def build_widget_frame(self, container):
        pass


    def build_treeview(self, container, row, col):
        
        columns = ['name', 'id', 'status']

        my_tree = ttk.Treeview(container, columns=columns, show='headings')
        my_tree.heading('name', text='Name')
        my_tree.heading('id', text='Id')
        my_tree.heading('status', text='Status')

        zones = []
        for zone in self.zones['result']:
            zones.append((zone['name'], zone['id'], zone['status']))

        for zone in zones:
            my_tree.insert('', tk.END, values=zone)


        def _item_selected(event):
            for selected_item in my_tree.selection():
                item = my_tree.item(selected_item)
                record = item['values']
                showinfo(title='Info', message=','.join(record))

        my_tree.bind('<<TreeviewSelect>>', _item_selected)
        my_tree.grid(row=row, column=col)


    def doNothing(self):
        print("Did Nothing")

    def settings(self, key):
        return SettingsScreen(key=key) 
        
if __name__ == '__main__':
    app = MainScreen()
    app.mainloop()
        