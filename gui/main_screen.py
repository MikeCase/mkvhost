import tkinter as tk
from tkinter import ttk
from cloudflare.cflare import CFlare
from gui.settings_screen import SettingsScreen
from gui.containers.main_screen_containers import TreeViewContainer, OptionsContainer


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

        opts_container = OptionsContainer()
        # opts_container.grid(row=0, column=0)


        tv_container = TreeViewContainer(opts_container.zone_name_sv, opts_container.zone_id_sv, opts_container.zone_status_sv)
        # tv_container.grid(row=1, column=0)

        

        # self.build_widget_frame(tv_container)
        if self.zones == None:
            self.settings(self.zones)
        else:
            tv_container.draw_widget(self.zones)
            opts_container.draw_widget()

        self.config(menu=menubar)



    def doNothing(self):
        print("Did Nothing")

    def settings(self, key):
        return SettingsScreen(key=key) 
        
# if __name__ == '__main__':
#     app = MainScreen()
#     app.mainloop()
        