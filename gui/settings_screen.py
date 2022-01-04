import tkinter as tk
from tkinter import ttk, StringVar
import os
import dotenv

class SettingsScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        dotenv.load_dotenv()
        
        self.title("Settings")
        self.geometry('400x300')

        api_key = StringVar(value=os.getenv('token'))
        api_email = StringVar(value=os.getenv('email'))
        
        lbl_frame = ttk.LabelFrame(self, text="Settings")
        lbl_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        lbl_api_key = tk.Label(lbl_frame, text="API Key")
        lbl_email = tk.Label(lbl_frame, text="Email Address")


        txt_api_key = tk.Entry(lbl_frame, width=45)
        txt_api_email = tk.Entry(lbl_frame, width=45)
        txt_api_key.insert(0, api_key.get())
        txt_api_email.insert(0, api_email.get())
        txt_api_email.bind("<Return>", lambda: set_api_email(txt_api_email.get()))
        txt_api_key.bind("<Return>", lambda: set_api_key(txt_api_key.get()))
        txt_api_email.grid(row=0, column=1, padx=5, pady=10)
        txt_api_key.grid(row=1, column=1, padx=5, pady=10)
        lbl_email.grid(row=0, column=0, padx=5, pady=10)
        lbl_api_key.grid(row=1, column=0, padx=5, pady=10)

        btn_save = tk.Button(self, text="Save", command=lambda: self.save_api_info())

        def save_api_info(self):
            with open('.env', 'w+') as env_file:
                env_file.write(f"EMAIL={api_email.get()}")
                env_file.write(f"TOKEN={api_key.get()}")
                
        def set_api_email(self, email):
            api_email.set(value=email)

        def set_api_key(self, token):
            api_key.set(value=token)