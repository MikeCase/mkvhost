### What is mkvhost

mkvhost is an app to simplify the process of creating a vhost on a server.
Will also connect to cloudflare and add a subdomain.  

### Usage

mkvhost -r [server-root] --host [vhost.domain.com]
mkvhost -r [server-root] -p y --host [vhost.domain.com] 

This will create a basic server using fpm to serve php files. 

EX:
sudo mkvhost -r /path/to/server/root --host example.domain.com -p y

