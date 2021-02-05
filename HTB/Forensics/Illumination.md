# Illumination

This forensics challenge is by hack the box and exploits leaving security breaches in git logs.

For this challenge you should download the given file and input the password when asked for.

This is what you see when opening for the first time

![Opened the zip](./OpenZip1.PNG)

Then I opened the Illumination.JS folder to see what is inside. This is what is inside.

![Opened first folder](./OpenZip2.PNG)

Then I opened to see the `config.json` file as config files can always tell us something about the program we are looking at. It is useful to note at this point that one of the folders there is names `.git` meaning this is most likely a git repository.

This is what we see when opening it:

```json
{



	"token": "Replace me with token when in use! Security Risk!",

	"prefix": "~",

	"lightNum": "1337",

	"username": "UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ==",

	"host": "127.0.0.1"



}
```
Hmmm, that top line is interesting. The token has been replaced for a security risk. These is a chance a developer has left this in the git logs. Thats what we can look at next. To do this just traverse in the terminal into the folder holding the `.git`. This is what you'll see when you use the command:

```bash
$ git log
```
![Git Logs](./GitLog.PNG)

That second one down looks interesting:

![Interesting Git Log](./InterestingGitLog.PNG)
