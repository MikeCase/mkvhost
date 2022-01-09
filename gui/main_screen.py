import tkinter as tk
from tkinter import ttk
from cloudflare.cflare import CFlare
from gui.settings_screen import SettingsScreen
from gui.containers.main_screen_containers import ScreenData, TreeViewContainer, OptionsContainer


class MainScreen(tk.Tk):
    def __init__(self, cflare: CFlare):
        super().__init__()
        self.cflare = cflare
        self.zones = self.cflare.show_zones()
        print(self.zones)
        for zone in self.zones['result']:
            # print(zone)
            self.zone_id_sv = zone['id']
            self.zone_name_sv = zone['name']
            self.zone_status_sv = zone['status']
        # sc = ScreenData(zone_id=self.zone_id, zone_name=self.zone_name, zone_status=self.zone_status)
        
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


        tv_container = TreeViewContainer()
        # tv_container.grid(row=1, column=0)

        

        # self.build_widget_frame(tv_container)
        ## This is a very bad way of handling this particular error. 
        if self.zones == None:
            self.settings(self.zones)
        else:
            tv_container.draw_widget()
            opts_container.draw_widget()

        self.config(menu=menubar)



    def doNothing(self):
        print("Did Nothing")

    def settings(self, key):
        return SettingsScreen(key=key) 
        
# if __name__ == '__main__':
#     app = MainScreen()
#     app.mainloop()
        