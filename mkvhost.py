import click
import requests
import os
import json
import CloudFlare
from pystache import render

homedir = os.environ['HOME']
username = os.environ['USER']

def my_ip():
    url = 'https://api.ipify.org'
    
    try:
        ip_address = requests.get(url).text
    except:
        exit('%s: failed' % (url))
    if ip_address == '':
        exit('%s: failed' % (url))
    if ':' in ip_address:
        ip_address_type = 'AAAA'
    else:
        ip_address_type = 'A'
    
    return ip_address, ip_address_type

def mkcfg(root, host, template, fpm):

    if os.path.isdir(f"{homedir}/vhosts/{host}/") is False:
            os.makedirs(f"{homedir}/vhosts/{host}/log/")

    alog = f"{homedir}/vhosts/{host}/log/access.log"
    elog = f"{homedir}/vhosts/{host}/log/error.log"

    root = ''.join((f"{homedir}/vhosts/{host}/{root}/"))

    with open(f"{homedir}/vhosts/{host}/{host}", 'w') as fp:
        if template is "php":
            with open(f"nginx-php{fpm}.tmpl", 'r') as tmpl:
                fp.write(render(tmpl.read(), locals()))

    
def mkdns(cf, host_name, zone_name, zone_id):

    ip_address, ip_address_type = my_ip()
    
    dns_name = f"{host_name}.{zone_name}"

    dns_records = [
        {
            'type':ip_address_type,
            'name':host_name,
            'content':ip_address,
            'proxied': True
        }
    ]

    try:
        for dns_record in dns_records:
            r = cf.zones.dns_records.post(zone_id, data=dns_record)
        
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones.dns_records.post %s - %d %s - api call failed' % (dns_name, e, e))

    print('CREATED: %s %s' % (dns_name, ip_address))

def deldns(cf, host, zone_id):
    
    dns_records = cf.zones.dns_records.get(zone_id, params={'name':host})
    for dns_record in dns_records:
        dns_record_id = dns_record['id']
        r = cf.zones.dns_records.delete(zone_id, dns_record_id)
    

@click.command()
@click.argument('root')
@click.argument('host')
@click.option('--template', '-t', default="php", help="Template to use..")
@click.option('--fpm', default="hhvm", help="hhvm or fpm")
@click.option('--remove', '-r', default=False, help="Remove Vhost")
@click.option('--public', '-p', default=False, help="Make site Live (Add cloudflare dns entry")
def cli(root, host, template, fpm, remove, public):
    """ 
    Setup cloudflare connection
    """
    cf = CloudFlare.CloudFlare()

    host_name, zone_name = host.split('.', 1)
    try:
        params = {'name':zone_name}
        zones = cf.zones.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones %d %s - api call failed' % (e, e))
    except Exception as e:
        exit('/zones.get - %s - api call failed' % (e))

    if len(zones) == 0:
        exit('/zones.get - %s - zone not found' % (zone_name))
    
    if len(zones) != 1:
        exit('/zones.get - %s - api call returned %d items' % (zone_name, len(zones)))

    zone = zones[0]
    zone_name = zone['name']
    zone_id = zone['id']

    if remove is False:
        mkcfg(root, host, template, fpm)
        if public is True:
            mkdns(cf, host_name, zone_name, zone_id)

    else:
        deldns(cf, host, zone_id)