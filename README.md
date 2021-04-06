### What is mkvhost

mkvhost is a tool that I created to speed up and simplify creating a 
Virtual Host on the NginX web-server.

# Big update 
I've completely redesigned the code, probably wont even be using the python-cloudflare api anymore
Tests are in the test folder, not sure if setup.py is working at the moment, haven't changed anything. 

Also I'd like to acknowledge that the original code I had posted was not my original work. I had copied
and pasted stuff together, then forgot about it forever.. It was essentially the stepping stone to this
current work. 

I have A LOT of work to do. Right now you can actually connect to the cloudflare API using your own .env file
with your email and key in it, (breakdown of file below). show a list of records, add a record and delete a record.


### Usage

* mkvhost [zone-name] [action] 
* mkvhost example.com add test.example.com (Some defaults are assumed.)
* mkvhost example.com del test.example.com (Again some defaults are assumed.)
* mkvhost example.com list . (Been to lazy to fix it at the moment. you have to add
                            the dot at the end, or something, haven't added a check
                            for missing 3rd argument)



### Future plans (Yes, I'm finally going to start working on this again)

Right now the biggest update that I can think about making is to add python
and other languages to the tool. 
