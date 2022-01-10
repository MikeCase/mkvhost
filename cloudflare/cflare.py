'''
.env should contain these two key/value pairs.

EMAIL = your-email-address
KEY = your-api-key

I've not been able to get it to work successfully with just token
authentication. Maybe not tested extensively enough. 

'''
import requests
from urllib.parse import urlparse, urlunparse
import json
import sys
import os
import pprint
from dotenv import load_dotenv
from requests.api import request


class CFlare:

    def __init__(self):
        """
        Initialize the cloudflare instance

        cf = CFlare()

        """

        load_dotenv()

        self.api_base_url = f"https://api.cloudflare.com/client/v4"

        self.api_email = os.getenv('EMAIL')
        self.api_key = os.getenv('KEY')

        self.headers = {
            'X-Auth-Email': self.api_email,
            'X-Auth-Key': self.api_key,
            'Content-Type':'application/json',
        }


    def build_api_path(self, params, query):
        """

        Build the API url.

        params: 
        query: The query string portion of the URL (ex. ?page=1&per_page=20)
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
        print(prepped_url)
        return prepped_url 


    def check_for_success(self, result):
        if result['success'] is True:
            return True
        else:
            return False


    ## Zones 
    def show_zones(self):
        q = f"page=1&per_page=20"
        params = ['zones']
        url = self.build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        zones = resp.json()
        resp.close()
        if self.check_for_success(zones):
            return zones
        else:
            return None
            

    def get_zone_id(self, zone_name: str = None):
        q = f"name={zone_name}&page=1&per_page=20"
        params = ['zones']
        url = self.build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        # print(resp.json())
        self.zone_id = resp.json()['result'][0]['id']
        resp.close()
        return self.zone_id

    def get_zone_records(self, zone_id: str = None):
        q = "page=1&per_page=20"
        params = ['zones', zone_id, 'dns_records']
        url = self.build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        zone_records = resp.json()
        resp.close()
        return zone_records

    def add_record(self, payload, zid):
        q=''
        params = ['zones', zid, 'dns_records']
        url = self.build_api_path(params, q)
        resp = requests.request("POST", url, headers=self.headers, data=payload)
        result = resp.json()
        resp.close()
        return result


    def get_record_by_name(self, zone_id, record_name):
        q=f'name={record_name}'
        params = ['zones', zone_id, 'dns_records']
        url = self.build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        rec_name = resp.json()
        resp.close()
        return rec_name
    
    def del_zone_record(self, zone_id, record_name):
        q=''
        q_id = self.get_record_by_name(zone_id, record_name)['result'][0]['id']
        params = ['zones', zone_id, 'dns_records', q_id]
        url = self.build_api_path(params, q)
        resp = requests.request("DELETE", url, headers=self.headers)
        result = resp.json()
        resp.close()
        return result

    def del_zone(self, zone_id):
        q = ''
        params = ['zones', zone_id]
        url = self.build_api_path(params, q)
        resp = requests.request("DELETE", url, headers=self.headers)
        result = resp.json()
        resp.close()
        return result

    def get_zone_details(self, zone_id):
        q=''
        params = ['zones', zone_id]
        url = self.build_api_path(params, q)
        resp = requests.request("GET", url, headers=self.headers)
        result = resp.json()
        resp.close()
        return result