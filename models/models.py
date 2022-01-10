from cloudflare.cflare import CFlare
import tkinter as tk
from pprint import pprint


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

    def get_zone_details(self, zone_id):
        zone_details = self.cflare.get_zone_details(zone_id)
        return zone_details

    def get_dns_records(self, z_id):
        zone_records = self.cflare.get_zone_records(z_id)
        # pprint(zone_records)
        zone_records = zone_records['result']
        zone_contents = []
        for contents in zone_records:
            ## Names of subdomains
            # zone_contents.append(contents['name'])
            
            ## Subdomain Id's
            # zone_contents.append(f"{contents['name']} - {contents['id']}")

            ## Creation date of subdomain
            zone_contents.append(f"{contents['name']} - {contents['created_on']}")

            ## Last modified date of subdomain
            # zone_contents.append(f"{contents['name']} {contents['modified_on']}")

            ## Can you use cloudflare proxies on this domain?
            # zone_contents.append(f"{contents['name']} - {contents['proxiable']}")

            ## Are you using cloudflare proxies on this domain?    
            # zone_contents.append(f"{contents['name']} - {contents['proxied']}")
            
            ## Type of dns record
            # zone_contents.append(f"{contents['name']} - {contents['type']}")


        # return zone_contents
        pprint(zone_contents)

    def get_api_key(self) -> str:
        self.api_key.get()

    def get_api_email(self) -> str:
        self.api_email.get()

    