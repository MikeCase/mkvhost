### What is mkvhost

mkvhost is a tool that I created to speed up and simplify creating a 
Virtual Host on the NginX web-server.

# Big update 
I've completely redesigned the code, probably wont even be using the python-cloudflare api anymore
Tests are in the test folder, not sure if setup.py is working at the moment, haven't changed anything. 

Also I'd like to acknowledge that the original code I had posted was not my original work. I had copied
and pasted stuff together, then forgot about it forever.. It was essentially the stepping stone to this
current work. 

### Usage

mkvhost [zone-name] [action] 
mkvhost [zone-name] [action] 

This will create a basic server using fpm to serve php files. 

EX:
```
sudo mkvhost -r /path/to/server/root --host example.domain.com -p y
```

Usage: mkvhost [OPTIONS]

```
Options:
    -r, --root TEXT      Set your root directory  [required]
    --host TEXT          Set your hostname  [required]
    -t, --template TEXT  Template to use..
    --fpm TEXT           hhvm or fpm
    -d, --remove         Remove Vhost
    -p, --public TEXT    Would you like your vhost to be public?
    --help               Show this message and exit.
```

### Future plans (Yes, I'm finally going to start working on this again)

Right now the biggest update that I can think about making is to add python
and other languages to the tool. 
