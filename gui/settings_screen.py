import tkinter as tk
from tkinter import ttk
import os
from dotenv import load_dotenv
from dotenv.main import dotenv_values

class SettingsScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        load_dotenv()
        config = dotenv_values()
        self.title("Settings")
        self.geometry('400x300')

        self.api_email = tk.StringVar()
        self.api_email.set(value=config['EMAIL'])
        self.api_key = tk.StringVar()
        self.api_key.set(value=config['TOKEN'])
        # print(self.api_email.get())
        lbl_frame = ttk.LabelFrame(self, text="Settings")
        lbl_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        lbl_api_key = tk.Label(lbl_frame, text="API Key")
        lbl_email = tk.Label(lbl_frame, text="Email Address")


        txt_api_email = tk.Entry(lbl_frame, textvariable=self.api_email, width=45,)
        txt_api_key = tk.Entry(lbl_frame, textvariable=self.api_key, width=45,)
        txt_api_email.insert(0,self.api_email.get())
        txt_api_key.insert(0, self.api_key.get())
        lbl_email.grid(row=0, column=0, padx=5, pady=10)
        lbl_api_key.grid(row=1, column=0, padx=5, pady=10)
        txt_api_email.grid(row=0, column=1, padx=5, pady=10)
        txt_api_key.grid(row=1, column=1, padx=5, pady=10)
        txt_api_email.bind("<Return>", lambda x=txt_api_email.get(): self.set_api_email(x))
        print(self.api_email.get())
        txt_api_key.bind("<Return>", lambda x=txt_api_key.get() : self.set_api_key(x))

        btn_save = tk.Button(self, text="Save", command=lambda x=self.api_email.get(), k=self.api_key.get(): self.save_api_info(x, k))
        btn_save.grid(row=1, column=0)


    def save_api_info(self, email, key):
        print(email, key)
        with open('.env', 'w+') as env_file:
            env_file.write(f"EMAIL = '{email}'\n")
            env_file.write(f"TOKEN = '{key}'\n")
            
    def set_api_email(self, email):
        print(f"Setting {self.api_email.get()} to {email}")
        self.api_email.set(value=email)
        print(f"Set {self.api_email.get()} to {email}")

    def set_api_key(self, token):
        self.api_key.set(value=token)