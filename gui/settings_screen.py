import tkinter as tk
from tkinter import ttk
import os
import dotenv

class SettingsScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        dotenv.load_dotenv()
        
        self.title("Settings")
        self.geometry('400x300')

        api_key = tk.StringVar()
        api_email = tk.StringVar()
        api_key.set(value=os.getenv('token'))
        api_email.set(value=os.getenv('email'))
        print(api_email.get())
        lbl_frame = ttk.LabelFrame(self, text="Settings")
        lbl_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        lbl_api_key = tk.Label(lbl_frame, text="API Key")
        lbl_email = tk.Label(lbl_frame, text="Email Address")


        txt_api_key = tk.Entry(lbl_frame, width=45, textvariable=api_key)
        txt_api_email = tk.Entry(lbl_frame, width=45, textvariable=api_email)
        txt_api_email.bind("<Return>", lambda x=txt_api_email.get(): api_email.set(value=x))
        txt_api_key.bind("<Return>", lambda x=txt_api_key.get(): api_key.set(value=x))
        txt_api_email.grid(row=0, column=1, padx=5, pady=10)
        txt_api_key.grid(row=1, column=1, padx=5, pady=10)
        lbl_email.grid(row=0, column=0, padx=5, pady=10)
        lbl_api_key.grid(row=1, column=0, padx=5, pady=10)

        btn_save = tk.Button(self, text="Save", command=lambda x=api_email.get(), v=api_key.get(): self.save_api_info(x, v))
        btn_save.grid(row=1, column=0)


    def save_api_info(self, email, key):
        with open('.env', 'w+') as env_file:
            env_file.write(f"EMAIL = '{email}'\n")
            env_file.write(f"TOKEN = '{key}'\n")
            
    def set_api_email(self, email):
        self.api_email.set(value=email)

    def set_api_key(self, token):
        self.api_key.set(value=token)