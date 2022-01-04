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

        self.api_key = StringVar()
        self.api_email = StringVar()

        lbl_frame = ttk.LabelFrame(self, text="Settings")
        lbl_frame.grid(row=0, column=0, sticky='nsew')

        lbl_api_key = tk.Label(lbl_frame, text="API Key")
        lbl_email = tk.Label(lbl_frame, text="Email Address")

        print(os.getenv('email'))
        self.get_api_email()
        self.get_api_key()

        txt_api_key = tk.Entry(lbl_frame, textvariable=self.api_key.get())
        txt_api_email = tk.Entry(lbl_frame, textvariable=self.api_email.get())
        txt_api_key.grid(row=0, column=1)
        txt_api_email.grid(row=1, column=1)
        lbl_api_key.grid(row=0, column=0)
        lbl_email.grid(row=1, column=0)

    def get_api_key(self):
        self.api_key.set(value=os.getenv('token'))

    def get_api_email(self):
        self.api_email.set(value=os.getenv('email'))
        