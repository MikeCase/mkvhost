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


class CFlare:

    def __init__(self, zone_name, email, token):
        """
        Initialize the cloudflare instance

        cf = CFlare(zone_name, email, token)

        zone_name: Name of the zone you want to use. 
        """
        self.zone_id = ''
        self.api_base_url = f"https://api.cloudflare.com/client/v4"
        self.zone_name = zone_name
        self.headers = {
            'X-Auth-Email': email,
            'X-Auth-Key': token,
            'Content-Type':'application/json',
        }
        
        

    def _build_api_path(self, params, query=''):
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

        # Failing at the moment.
    def show_zones(self):
        zones = []
        q = f"page=1&per_page=20"
        params = ['zones']
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        cntr = 0
        if len(resp.json()['result']) > 1:
            for zone in resp.json()['result']:
                for x in zone[cntr]:
                    zones.append(x['id'])
                    cntr + 1
        else:
            zones.append(resp.json()['result'][0]['id'])
        return zones

    def get_zone_id(self):
        q = f"name={self.zone_name}&page=1&per_page=20"
        params = ['zones']
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        zone_id = resp.json()['result'][0]['id']
        self.zone_id = zone_id
        return zone_id

    def get_records(self):
        q = "page=1&per_page=20"
        params = ['zones', self.zone_id, 'dns_records']
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        zone_records = resp.json()['result']
        return zone_records

    def add_record(self, payload, zid):
        params = ['zones', zid, 'dns_records']
        url = self._build_api_path(params)

        resp = requests.request("POST", url, headers=self.headers, data=payload)
        result = resp.json()
        
        return result


    def get_record_by_name(self, zone_id, record_name):
        ''' Get the record name and return the id '''
        print(record_name)
        q=f'name={record_name}'
        params = ['zones', zone_id, 'dns_records']
        url = self._build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        try:
            rec_id = resp.json()['result'][0]['id']
        except IndexError as e:
            rec_id = {"success": False, "error": f"No record found: {e}"}
        # breakpoint()
        return rec_id
    
    def del_record(self, zone_id, record_name):
        q_id = self.get_record_by_name(zone_id, record_name)
        # breakpoint()
        params = ['zones', zone_id, 'dns_records', q_id]
        url = self._build_api_path(params)
        breakpoint()
        resp = requests.request("DELETE", url, headers=self.headers)
        result = resp.json()
        return result