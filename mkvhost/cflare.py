'''
.env should contain these two key/value pairs.

email = your-email-address
token = your-api-key

I've not been able to get it to work successfully with just token
authentication. Maybe not tested extensively enough. 

'''
import requests
from urllib.parse import urlparse, urlunparse
import json
import sys
import os
import pprint
import dotenv


class CFlare:

    def __init__(self, zone_name):
        """
        Initialize the cloudflare instance

        cf = CFlare(zone_name)

        zone_name: Name of the zone you want to use. 
        """

        self.api_base_url = f"https://api.cloudflare.com/client/v4"
        self.zone_name = zone_name
        dotenv.load_dotenv()
        self.headers = {
            'X-Auth-Email': os.getenv('email'),
            'X-Auth-Key':os.getenv('token'),
            'Content-Type':'application/json',
        }
        
        self.zone_id='c4f876ffa36284d86ce9145148994eee'




    def _build_api_path(self, params, query):
        """
        params in this case are any parameters that the url will accept.
        such as anything after zones. the zone id till you get to the query string

        """
        

        self.url = urlparse(self.api_base_url)
        self.params = params
        self.query = query
        self.api_path = ['client/v4']
        if len(self.params) > 0:
            for i in range(0,len(self.params)):
                self.api_path.append(f'/{self.params[i]}')
        
        self.final_path = ''.join(self.api_path)
        builturl = [
            f'{self.url.scheme}',
            f'{self.url.hostname}', 
            f'{self.final_path}', 
            f'{self.url.params}', 
            f'{self.query}', 
            f'{self.url.fragment}',
        ]
        prepped_url = urlunparse(builturl)

        return prepped_url 

        

    def show_zones(self):
        q = f"page=1&per_page=20"
        params = ['zones', self.zone_id]
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        zones = resp.json()
        resp.close()
        return zones

    def get_zone_id(self):
        q = f"name={self.zone_name}&page=1&per_page=20"
        params = ['zones']
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        self.zone_id = resp.json()['result'][0]['id']
        resp.close()
        return self.zone_id

    def get_records(self):
        q = "page=1&per_page=20"
        params = ['zones', self.zone_id, 'dns_records']
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        zone_records = resp.json()
        resp.close()
        return zone_records

    def add_record(self, payload, zid):
        q=''
        params = ['zones', zid, 'dns_records']
        url = self._build_api_path(params, q)
        resp = requests.request("POST", url, headers=self.headers, data=payload)
        result = resp.json()
        resp.close()
        return result


    def get_record_by_name(self, zone_id, record_name):
        q=f'name={record_name}'
        params = ['zones', zone_id, 'dns_records']
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        rec_name = resp.json()
        resp.close()
        return rec_name
    
    def del_record(self, zone_id, record_name):
        q=''
        q_id = self.get_record_by_name(zone_id, record_name)['result'][0]['id']
        params = ['zones', zone_id, 'dns_records', q_id]
        url = self._build_api_path(params, q)
        resp = requests.request("DELETE", url, headers=self.headers)
        result = resp.json()
        resp.close()
        return result