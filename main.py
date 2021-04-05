import requests
import json
import sys
import os
from mkvhost.cflare import CFlare
import pprint


sys.path.insert(0, os.path.abspath('..'))
zone_name = sys.argv[1]
# print(zone_name)


def main():

    cf = CFlare(zone_name)
##
    zone_id = cf.get_zone_id()
    # cf.show_zones()
    records = cf.get_records()
    # pprint.pprint(records)
    if sys.argv[2] and sys.argv[3]:
        if sys.argv[2] == 'add':
            payload = json.dumps({
                "type": "A",
                "name":f'{sys.argv[3]}',
                "content": "45.79.42.59",
                "ttl": "1",
                "proxied": True,
            })
            result = cf.add_record(payload, zone_id)
            print(f"Name: {result['result']['name']}")
            print(f"Id: {result['result']['id']}")
            
        if sys.argv[2] == 'del':
            result = cf.del_record(zone_id, sys.argv[3])
            print(f"Success: {result['success']}")

        if sys.argv[2] == 'list':
            for record in cf.get_records():
                print(f"Name: {record['name']}")
                print(f"Id: {record['id']}")
    else:
        pass

if __name__ == "__main__":
    
    main()