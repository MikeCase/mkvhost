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
        self.record_id: str = tk.StringVar()
        self.record_name: str = tk.StringVar()
        self.record_type: str = tk.StringVar()
        self.records = []

    def get_zones(self) -> list:
        zones = self.cflare.show_zones()
        zones = zones['result']
        return zones

    def get_zone_details(self, zone_id):
        zone_details = self.cflare.get_zone_details(zone_id)
        return zone_details


    def get_dns_record(self, z_id, r_id):
        dns_record = self.cflare.get_record_by_id(z_id, r_id)
        pprint(dns_record)


    def get_dns_records(self, z_id):
        zone_records = self.cflare.get_zone_records(z_id)
        # pprint(zone_records)
        zone_records = zone_records['result']
        zone_contents = []
        for contents in zone_records:

            ''' DNS Record fields.
            ## 
            ## 'id': record ID
            ## 'name': record name
            ## 'created_on': Datetime record was created
            ## 'modified_on': Datetime record was modified
            ## 'proxiable': is record proxiable?
            ## 'proxied': is record proxied through cloudflare
            ## 'type': record type
            ## 'locked': 
            ## 'ttl':
            ## '':
            ## '':
            # '''

            self.records.append(
                {
                    'id': contents['id'],
                    'name': contents['name'],
                    'created_on': contents['created_on'],
                    'modified_on': contents['modified_on'],
                    'locked': contents['locked'],
                    'proxiable': contents['proxiable'],
                    'proxied': contents['proxied'],
                    'ttl': contents['ttl'],
                    'type': contents['type'],
                }
            )

        # self.records.set(value=zone_contents)
        print("Records: \n")
        pprint(self.records)
        # print("Contents: \n")
        # pprint(zone_contents)
        # return zone_contents
        # pprint(zone_contents)

    def get_api_key(self) -> str:
        self.api_key.get()

    def get_api_email(self) -> str:
        self.api_email.get()

    