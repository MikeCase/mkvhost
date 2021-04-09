import requests
import json
import sys
import os
from mkvhost.cflare import CFlare
import pprint
import dotenv

# sys.path.insert(0, os.path.abspath('..'))
zone_name = sys.argv[1]
dotenv.load_dotenv()
email = os.getenv('email')
token = os.getenv('token')
zone_name = os.getenv('host_name')
zone_id = os.getenv('zone_id')
server_ip = os.getenv('server_ip')

# Hack? It works, I'll worry about it later. 
with open('tests/testpayload.json', 'r') as jfile:
    test_payload = json.load(jfile)
    test_payload['proxied'] = True

print(test_payload)
def main():
    # Initialize Cloudflare instance.
    cf = CFlare(zone_name, email, token)

    # If arguments 2 and 3 have values]
    # Check argument 2 for the action word
    # after we know the action word we can know
    # what to do with argument 3
    if sys.argv[2]:
        if len(sys.argv) > 3:
            if sys.argv[2] == 'add':
                payload = json.dumps(test_payload)
                print(payload)
                # breakpoint()
                result = cf.add_record(payload, zone_id)
                # print(result)
                # print(f"Name: {result['result']['name']}")
                # print(f"Id: {result['result']['id']}")
            
            if sys.argv[2] == 'del':
                result = cf.del_record(zone_id, sys.argv[3])
                print(f"Success: {result['success']}")

        if sys.argv[2] == 'list':

            filename = 'dns_list.txt'
            if os.path.exists(filename) & os.path.isfile(filename):
                os.unlink(filename)

            for record in cf.get_records():
                filecontents = f"Name: {record['name']}\t\tType: {record['type']}\n"
                filecontents += '-'*40+'\n'
                filecontents += f"Id: {record['id']} \n"
                filecontents += f"Content: {record['content']} \n"
                filecontents += '-'*40+'\n'
                filecontents += '\n'

                with open(filename, 'a') as temp:
                    temp.write(filecontents)


if __name__ == "__main__":
    
    main()