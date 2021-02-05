# USB RIPPER

This a write-up to the hack the box challenge USB RIPPER.

![files](./Files.PNG)

These are the files that have to be downloaded, in them are a JSON file of all the authenticated devices with their serial numbers, product numbers and manufacturer numbers.

The syslog file is a dump of all of the logs of a device that had data exfiltrated from it from a USB.

If we have both of those then we can make a script that gets the one serial number that isn't in the authenticated as that should be the devices that took the data.

This can be done with a script, I made mine in python.

```python
import re
import json

file1 = open("syslog", 'r')
lines1 = file1.readlines()

file2 = open("auth.json", 'r')
jsonLog = file2.read()
jsonArrayS = json.loads(jsonLog)["serial"]



r = re.compile("usb \d-\d: SerialNumber: ([0-9A-F]+)")
for l in lines1:
  m = r.search(l, 0)
  if m is not None:
    hexcode = m.group(1)
    if hexcode not in jsonArrayS:
        print(hexcode)
```

There are some important things to note about this script. First there are 3 arrays that are in the JSON so you need to maker sure the right one is used for the equality checks. This is `jsonArrayS = json.loads(jsonLog)["serial"]`.

In the log files we need to clear everything we don't need to get a list of serial numbers, I did this with a regex. `r = re.compile("usb \d-\d: SerialNumber: ([0-9A-F]+)")`

Lastly python uses in for JSON so we used `not in` so that the one that is not there is produced in the print statement.

The output will be a string hashed to length 32, length 32 strings that are hashed are md5 hashed. Just put `HTB{[hash cracked string]}` into your hack that box flag submission and that is the flag for the challenge
