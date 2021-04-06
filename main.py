import requests
import json
import sys
import os
from mkvhost.cflare import CFlare
import pprint


# sys.path.insert(0, os.path.abspath('..'))
zone_name = sys.argv[1]
# print(zone_name)


def main():
    # Initialize Cloudflare instance.
    cf = CFlare(zone_name)

    # Get the zone id for use in subsequent calls.
    zone_id = cf.get_zone_id()

    # Get a list of all the records. 
    records = cf.get_records()
    # pprint.pprint(records)

    # If arguments 2 and 3 have values]
    # Check argument 2 for the action word
    # after we know the action word we can know
    # what to do with argument 3
    if sys.argv[2]:
        if len(sys.argv) > 3:
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

            filename = 'dns_list.txt'
            if os.path.exists(filename) & os.path.isfile(filename):
                os.unlink(filename)

            for record in cf.get_records()['result']:
                filecontents = f"Name: {record['name']}\t\tType: {record['type']}\n"
                filecontents += '-'*40+'\n'
                filecontents += f"Id: {record['id']} \n"
                filecontents += f"Content: {record['content']} \n"
                filecontents += '-'*40+'\n'
                filecontents += '\n'

                with open(filename, 'a') as temp:
                    temp.write(filecontents)
                    # temp.close()
    else:
        pass

if __name__ == "__main__":
    
    main()