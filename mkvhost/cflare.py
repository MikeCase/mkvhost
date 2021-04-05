import requests
import json
import sys
import os
import pprint
import dotenv
class CFlare:

    def __init__(self, zone_name):
        # Initialize the cloudflare instance
        self.api_base_url = f"https://api.cloudflare.com/client/v4"
        self.zone_name = zone_name
        dotenv.load_dotenv()
        self.headers = {
            'X-Auth-Email': os.getenv('email'),
            'X-Auth-Key':os.getenv('token'),
            'Content-Type':'application/json',
        }
        
#
        self.zone_id='c4f876ffa36284d86ce9145148994eee'
        # try:
        #     self.cf = CloudFlare.CloudFlare()
        # except Exception as e:
        #     print(f'Something didn\'t click... {e}')
        #     exit(0)

    def show_zones(self):
        q = f"?page=1&per_page=20"
        url = ''.join([self.api_base_url, "/zones", f'{q}'])
        resp = requests.request("GET", url, headers=self.headers)
        zones = resp.json()
        # pprint.pprint(zones)
        resp.close()
        return zones

    def get_zone_id(self):
        q = f"?name={self.zone_name}&page=1&per_page=20"
        url = ''.join([self.api_base_url, "/zones", f'{q}'])
        resp = requests.request("GET", url, headers=self.headers)
        self.zone_id = resp.json()['result'][0]['id']
        resp.close()
        return self.zone_id

    def get_records(self):
        q = "?page=1&per_page=20"
        # print(self.zone_id)
        url = ''.join([self.api_base_url, '/zones', f'/{self.zone_id}', '/dns_records', f'{q}'])
        # print(url)
        resp = requests.request("GET", url, headers=self.headers)
        zone_records = resp.json()
        resp.close()
        return zone_records

    def add_record(self, payload, zid):
        q=''
        url = ''.join([self.api_base_url, '/zones', f'/{zid}', '/dns_records'])
        resp = requests.request("POST", url, headers=self.headers, data=payload)
        # pprint.pprint(resp.json())
        result = resp.json()
        resp.close()
        return result


    def get_record_by_name(self, zone_id, record_name):
        q=f'?name={record_name}'
        url = ''.join([self.api_base_url, '/zones', f'/{zone_id}', '/dns_records', q])
        resp = requests.request("GET", url, headers=self.headers)
        # pprint.pprint(resp.json())
        resp.close()
        return resp.json()
    
    def del_record(self, zone_id, record_id):
        q=''
        url = ''.join([self.api_base_url, '/zones', f'/{zone_id}', '/dns_records/', f'{record_id}'])
        # print(url)
        resp = requests.request("DELETE", url, headers=self.headers)
        # print('delete_records')
        # pprint.pprint(resp.json())
        resp.close()
        return resp.json()