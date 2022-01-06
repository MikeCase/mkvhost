import tkinter as tk
from tkinter import ttk
import os
from dotenv import load_dotenv
from dotenv.main import dotenv_values

class SettingsScreen(tk.Toplevel):
    def __init__(self, key=None):
        super().__init__()

        load_dotenv()
        # config = dotenv_values()
        self.title("Settings")
        self.geometry('400x300')

        self.api_email = tk.StringVar()
        self.api_email.set(value=os.getenv("EMAIL"))
        self.api_key = tk.StringVar()
        self.api_key.set(value=os.getenv("KEY"))
        # print(self.api_email.get())
        lbl_frame = ttk.LabelFrame(self, text="Settings")
        lbl_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        lbl_api_key = tk.Label(lbl_frame, text="API Key")
        lbl_email = tk.Label(lbl_frame, text="Email Address")


        txt_api_email = tk.Entry(lbl_frame, textvariable=self.api_email, width=45,)
        txt_api_key = tk.Entry(lbl_frame, textvariable=self.api_key, width=45,)
        lbl_email.grid(row=0, column=0, padx=5, pady=10)
        lbl_api_key.grid(row=1, column=0, padx=5, pady=10)
        txt_api_email.grid(row=0, column=1, padx=5, pady=10)
        txt_api_key.grid(row=1, column=1, padx=5, pady=10)
        txt_api_email.bind("<Tab>", lambda x: self.set_api_email(txt_api_email.get()))
        print(self.api_email.get())
        txt_api_key.bind("<Tab>", lambda x: self.set_api_key(txt_api_key.get()))

        btn_save = tk.Button(self, text="Save", command=lambda: self.save_api_info())
        btn_save.grid(row=1, column=0)

        if key is None:
            self.raise_window()

    def raise_window(self):
        self.attributes('-topmost', True)


    def save_api_info(self):
        # print(email, key)
        """ Save the email and key to the .env file """
        email = self.api_email.get()
        key = self.api_key.get()
        with open('.env', 'w+') as env_file:
            env_file.write(f"EMAIL = '{email}'\n")
            env_file.write(f"KEY = '{key}'\n")

        if self.attributes('-topmost') is True:
            self.attributes('-topmost', False)


        
            
    def set_api_email(self, email):
        """ Set the API Email """
        self.api_email.set(value=email)

    def set_api_key(self, key):
        """ Set the API Key """
        self.api_key.set(value=key)