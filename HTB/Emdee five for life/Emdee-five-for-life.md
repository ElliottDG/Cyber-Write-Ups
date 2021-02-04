# Emdee five for life

This is a write for the Hack the box challenge Emdee five for life which requires you to get a string, hash with md5 and post it back to the server with a script.

For this script I used python3

To start, I did some reconnaissance on the page. I first looked at the home page.

![front page]('./FrontPage.PNG')

Then clicked the button on the home page.

![front page button clicked]('./FrontPage2.PNG')

Ok so this needs to be done very quickly, for this to be as quick as needed I made a script to do this.

Before I started making the script, I knew I had to make 1 GET request to get the string to be hashed and a post.

I can assume the GET request will just get the page so all of the content, including html tags.

For the post, I just need to see the format of the data.

![Post body]('./PostHash.md')
