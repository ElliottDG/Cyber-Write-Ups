# Mr Robot CTFS

Mr Robot CTF is a CTF that uses a brute force attack and linux priv esc once access is gained to a user server side.

## Flag 1

First things first, always with these I drop an nmap using `nmap -p- -T5 <ip>`. Warning doing -T5 will be very loud and slow down the network you're pinging so possibly use `-T4` or `-T3` if too much.

![nmap scan](./nmap.PNG)

Port 22 could be used later for ssh, for sure means there is a backend server to connect to somewhere.
Ports 80 and 443 open so this is a webserver and we can go to the website.

The site gives a fake terminal with different commands playing clips or showing images. Not much we can do with it.

Putting in a random extension to the URL will show a wordpress 404 page. Knowing this we can possibly use some wordpress vulnerabilities.

Looking at the hint on key 1 being "robots" and doing a dirbuster we can see `/robots` is a 200 OK response.

![dirb](./drib.PNG)

Going there reveals a file we can assess by pasting it as an extension next to the URL.

Along with this we get a .dic file which when opened is a wordlist. Possibly something that can be used later.
