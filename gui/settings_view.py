import tkinter as tk
from tkinter import ttk
from gui.views import View

class SettingsView(View):
    def __init__(self, master=None, model=None):
        super().__init__(master)
        self.master = master
        self.model = model

    def create_view(self):
        lbl_frame = ttk.LabelFrame(self, text="Settings")
        lbl_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        lbl_api_key = tk.Label(lbl_frame, text="API Key")
        lbl_email = tk.Label(lbl_frame, text="Email Address")


        txt_api_email = tk.Entry(lbl_frame, textvariable=self.model.api_email, width=45,)
        txt_api_key = tk.Entry(lbl_frame, textvariable=self.model.api_key, width=45,)
        lbl_email.grid(row=0, column=0, padx=5, pady=10)
        lbl_api_key.grid(row=1, column=0, padx=5, pady=10)
        txt_api_email.grid(row=0, column=1, padx=5, pady=10)
        txt_api_key.grid(row=1, column=1, padx=5, pady=10)
        txt_api_email.bind("<Tab>", lambda x: self.set_api_email(txt_api_email.get()))
        txt_api_key.bind("<Tab>", lambda x: self.set_api_key(txt_api_key.get()))

        btn_save = tk.Button(self, text="Save", command=lambda: self.save_api_info())
        btn_save.grid(row=1, column=0)



    def save_api_info(self):
        # print(email, key)
        """ Save the email and key to the .env file """
        email = self.api_email.get()
        key = self.api_key.get()
        with open('.env', 'w+') as env_file:
            env_file.write(f"EMAIL = '{email}'\n")
            env_file.write(f"KEY = '{key}'\n")



        
            
    def set_api_email(self, email):
        """ Set the API Email """
        self.model.api_email.set(value=email)

    def set_api_key(self, key):
        """ Set the API Key """
        self.model.api_key.set(value=key)