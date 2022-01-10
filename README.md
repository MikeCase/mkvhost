### What is mkvhost

mkvhost is a tool that I created to speed up and simplify creating a 
Virtual Host on the NginX web-server.


# Big update 
I've completely redesigned the code(Again), ~~probably wont even be using the python-cloudflare api anymore~~ Definately am not using the python-cloudflare module anymore. I've started work on my own module using requests. VERY VERY early design. I'm using tkinter and made a basic interface for the app. I've gotten around to drilling MVC into my thick skull so I believe the code is much better optimized. I still have a lot of work to do, and I have other projects I want to keep working on. So it may go slow. This also isn't my day job unfortunately so it'll be slow going. 
~~Tests are in the test folder,~~ They're there, but I've kind of abandond them, maybe I'll come back to them. Testing has been something I've had a hard time with understanding and nailing down. anyways, the cflare module I'm working on now needs to be separated into it's own project but it's still a part of this one.. I need to work on uncoupling them.  ~~not sure if setup.py is working at the moment, haven't changed anything~~ good luck with that, this is now a full blown app not just a module.. Something else thats in the works. See I think about these things, it's just a matter of if I ever get around to sitting down and learning the stuff I need to implement it.  

Also I'd like to acknowledge that the original code I had posted was not my original work. I had copied
and pasted stuff together, then forgot about it forever.. It was essentially the stepping stone to this
current work. 

I have A LOT of work to do. Right now you can actually connect to the cloudflare API using your own .env file
with your email and key in it, (breakdown of file below). show a list of records, add a record and delete a record.

I have a lot of updates to make to this file as well. 

Here's the long and short of it. If you want to run this, 
* clone it
* setup a virtual environment
* run pip install -r requirements.txt 
* run python main.py
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


### Issues

* Currently setup.py doesn't install correctly
* There's only six tests. 
* It's grosely lacking features
* Commenting is shit.
* Documentation lacking
* I'm working on it. 
* Not my day job.
* Wish it was. 
* Call me, maybe?