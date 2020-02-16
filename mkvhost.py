import click
import requests
import os
import shutil
import json
import CloudFlare
import subprocess
from pystache import render

## Virtual host config files ##
confavail = "/etc/nginx/sites-available"
confenabled = "/etc/nginx/sites-enabled"

if os.environ.get('SUDO_USER') is None:
    exit("Must run as root")
else:
    username = os.environ['SUDO_USER']
    userhome = os.path.expanduser(f"~{username}")


def my_ip():
    url = 'https://api.ipify.org'

    try:
        ip_address = requests.get(url).text
    except:
        exit(f'{url}: failed')
    if ip_address == '':
        exit(f'{url}: failed')
    if ':' in ip_address:
        ip_address_type = 'AAAA'
    else:
        ip_address_type = 'A'

    return ip_address, ip_address_type


def mkcfg(root, host, template, fpm):

    if os.path.isdir(f"{userhome}/vhosts/{host}/") is False:
        os.makedirs(f"{userhome}/vhosts/{host}/log/")

    alog = f"{userhome}/vhosts/{host}/log/access_log"
    elog = f"{userhome}/vhosts/{host}/log/error_log"

    root = ''.join((f"{userhome}/vhosts/{host}/"))

    with open(f"{confavail}/{host}", 'w') as fp:
        if template is "php":
            with open(f"nginx-php{fpm}.tmpl", 'r') as tmpl:
                fp.write(render(tmpl.read(), locals()))

    with open(f"{userhome}/vhosts/{host}/index.html", 'w') as fp:
        with open("index.tmpl", 'r') as tmpl:
            fp.write(render(tmpl.read(), locals()))


def mkdns(cf, host_name, zone_name, zone_id):
    host = f"{host_name}.{zone_name}"
    os.symlink(f"{confavail}/{host}", f"{confenabled}/{host}")

    ip_address, ip_address_type = my_ip()

    dns_name = f"{host_name}.{zone_name}"

    dns_records = [
        {
            'type': ip_address_type,
            'name': host_name,
            'content': ip_address,
            'proxied': True
        }
    ]

    try:
        for dns_record in dns_records:
            r = cf.zones.dns_records.post(zone_id, data=dns_record)

    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit(f'/zones.dns_records.post {dns_name} - {e} {e} - api call failed')

    print(f'CREATED: {dns_name} {ip_address}')
    subprocess.run(["service", "nginx", "reload"])


def deldns(cf, host, zone_id):

    dns_records = cf.zones.dns_records.get(zone_id, params={'name': host})
    for dns_record in dns_records:
        dns_record_id = dns_record['id']
        r = cf.zones.dns_records.delete(zone_id, dns_record_id)

    delvhost(host)


def delvhost(host):
    confavailName = f"{confavail}/{host}"
    vdir = f"{userhome}/vhosts/{host}"
    enabled_file = f"{confenabled}/{host}"

    if os.path.exists(enabled_file) and os.path.islink(enabled_file):
        os.unlink(enabled_file)

    if os.path.exists(confavailName) and os.path.isfile(confavailName):
        os.remove(confavailName)

    if os.path.exists(vdir) and os.path.isdir(vdir):
        shutil.rmtree(vdir)

    subprocess.run(["service", "nginx", "reload"])


@click.command()
@click.option('--root', '-r', required=True, help="Set your root directory")
@click.option('--host', required=True, help="Set your hostname")
@click.option('--template', '-t', default="php", help="Template to use..")
@click.option('--fpm', default="fpm", help="hhvm or fpm")
@click.option('--remove', '-d', is_flag=True, help="Remove Vhost")
@click.option('--public', '-p', default=None, help="Would you like your vhost to be public?")
def cli(root, host, template, fpm, remove, public):

    cf = CloudFlare.CloudFlare(debug=True)

    """ 
    Setup cloudflare connection
    """

    host_name, zone_name = host.split('.', 1)
    try:
        params = {'name': zone_name}
        zones = cf.zones.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit(f'/zones {e} {e} - api call failed')
    except Exception as e:
        exit(f'/zones.get - {e} - api call failed')

    if len(zones) == 0:
        exit(f'/zones.get - {zone_name} - zone not found')

    if len(zones) != 1:
        exit(
            f'/zones.get - {zone_name} - api call returned {len(zones)} items')

    zone = zones[0]
    zone_name = zone['name']
    zone_id = zone['id']

    if remove is True:
        print("Removing DNS entry...")
        deldns(cf, host, zone_id)
    else:
        mkcfg(root, host, template, fpm)
        if public is not None:
            mkdns(cf, host_name, zone_name, zone_id)
