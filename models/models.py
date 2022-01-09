from cloudflare.cflare import CFlare
import tkinter as tk


class CloudFlare:

    def __init__(self) -> None:
        self.cflare = CFlare()
        self.api_email: str = tk.StringVar()
        self.api_email.set(value=self.cflare.api_email)
        self.api_key: str = tk.StringVar()
        self.api_key.set(value=self.cflare.api_key)
        self.zone_id: str = tk.StringVar()
        self.zone_name: str = tk.StringVar()
        self.zone_status: str = tk.StringVar()
        self.zone_owner: str = tk.StringVar()

    def get_zones(self) -> list:
        zones = self.cflare.show_zones()
        zones = zones['result']
        return zones


    def get_api_key(self) -> str:
        self.api_key.get()

    def get_api_email(self) -> str:
        self.api_email.get()

    