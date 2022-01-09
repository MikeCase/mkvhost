import tkinter as tk
from abc import abstractmethod


class View(tk.Frame):
    @abstractmethod
    def create_view():
        raise NotImplementedError