# Took The Byte

This is a hack the box challenge that looks at recovering a file by suing an XOR to find the original type.

In this challenge we get given a file called `password` and this file cannot be opened.

The first thing I did was binwalk the file to see if that would display anything but it did not.

After that the next step was to xxd the file and see what comes up. This is that below:
